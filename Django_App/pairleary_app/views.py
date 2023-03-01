from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Orders
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import EmailMessage
from datetime import date

# 新規登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender_type = request.POST['gender']
        try:
            CustomUser.objects.create_user(username=username, email=email, password=password, **{'gender_type': gender_type})
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録済みです。'})
    return render(request, 'signup.html')

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mypage')
        else:
            return redirect('signup')
    return render(request, 'login.html', {})

# ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')

# マイページ
@login_required(login_url='/login/')
def mypage(request):
    user = request.user
    # ユーザーIDがログインしているユーザーと一致する予約情報を取得
    order_data = Orders.objects.filter(user_id_id=user)
    # マッチングが成立している自分のデータを取得
    matched_order_data = Orders.objects.filter(matched_user_id__isnull=False, matched_user_id=user)
    # 削除ボタンを押した予約を削除する
    if request.method == "POST" and 'delete_order' in request.POST:
        print(request.POST)
        order_id = request.POST.get('delete_order')
        order = Orders.objects.get(order_id=order_id)
        if order.matched_user_id is None:
            order.delete()
            return redirect('mypage')
        else:
            return render(request, 'mypage.html', {'order_data': order_data, 'matched_order_data':matched_order_data, 'error_message': 'この予約は削除できません。'})
    # 画面側から送られてきた箇所をアップデートする
    if request.method == 'POST':
        try:
            # ユーザー名の編集
            if 'username' in request.POST:
                user = request.user
                new_username = request.POST.get('username')
                user.username = new_username
                user.save()
                return redirect('mypage')
            # メールアドレスの編集
            if 'email' in request.POST:
                user = request.user
                new_email = request.POST.get('email')
                user.email = new_email
                user.save()
                return redirect('mypage')
            # 性別の編集
            if 'gender' in request.POST:
                user = request.user
                new_gender = request.POST.get('gender')
                user.gender_type = new_gender
                user.save()
                return redirect('mypage')
            # パスワードの編集
            if 'presentPassword' or 'newPassword' or 'confirmPassword' in request.POST:
                # 現在のパスワード
                presentPassword = request.POST.get('presentPassword')
                # 新しいパスワード
                newPassword = request.POST.get('newPassword')
                # 新しいパスワードの確認用
                confirmPassword = request.POST.get('confirmPassword')
                # 現在のパスワードのチェック
                if check_password(presentPassword, user.password):
                    try:
                        # 新しいパスワードと確認用パスワードのチェック
                        if newPassword == confirmPassword:
                            hashed_password = make_password(newPassword)
                            user.password = hashed_password
                            user.save()
                        else:
                            return render(request, 'mypage.html', {'error': '確認のためのパスワードが一致しません。'})
                    except IntegrityError:
                        return render(request, 'mypage.html', {'error': '現在のパスワードが一致しません。'})
                # セッションを再認証する
                user = authenticate(username=user.username, password=newPassword)
                if user is not None:
                    login(request, user)
                return redirect('mypage')
        except IntegrityError:
            return render(request, 'mypage.html', {'error': '問題が発生しました。リロードしてください。'})
    return render(request, 'mypage.html', {'order_data': order_data, 'matched_order_data':matched_order_data})

# マッチング新規予約
@login_required(login_url='/login/')
def create_order(request):
    if request.method == 'POST':
        try:
            Orders.objects.create(
                order_date=request.POST['date'],  # マッチング日付
                order_time_range_type=request.POST['time'],  # マッチング時間帯
                category=request.POST['purpose'],  # 目的（カテゴリ）
                hope_gender_type=request.POST['gender'],  # 希望する相手の性別
                comment=request.POST['comment'],  # コメント
                user_id_id=request.user.id  # user_id
                )
        except Exception:
            return render(request, 'create_order.html', {'error': '全ての希望条件を選択してください'})
        else:
            return redirect('search_matching')
    else:
        return render(request, 'create_order.html')


@login_required(login_url='/login/')  # ログインしているユーザーにのみ表示される
# マッチング検索機能
def search_matching(request):
    if request.method == "POST":
        # フォームから入力された条件を受け取る
        category = request.POST.get("purpose")
        gender = request.POST.get("gender")
        # ordersテーブルからカテゴリがcategory、性別がどちらでもOK、マッチング相手がいないデータを取得
        if gender == 'どちらでもOK':
            orders = Orders.objects.filter(
                category=category,
                matched_user_id__isnull=True,
                order_date__gte=date.today(),  # 今日の日付以降のデータのみを取得する
                ).exclude(user_id=request.user).select_related('user_id')
        else:
            # ordersテーブルからカテゴリがcategory、性別がgender、マッチング相手がいないデータを取得
            orders = Orders.objects.filter(
                category=category,
                matched_user_id__isnull=True,
                user_id__gender_type=gender,
                order_date__gte=date.today(),  # 今日の日付以降のデータのみを取得する
                ).exclude(user_id=request.user).select_related('user_id')
        if orders:
            context = {'orders': orders}
        else:
            context = {'error_message': '条件に一致するデータがありません'}
    else:
        context = {}

    # 申し込みボタンが押された場合
    # matched_user_idにボタンを押した人のuser_idを追加
    if request.method == "POST" and 'matching_button' in request.POST:
        order_id = request.POST.get('order_id')
        order = Orders.objects.get(pk=order_id)
        order.matched_user_id = request.user
        order.save()

        # マッチング成立後メールをBCCで送信するための処理
        bcc_list = [order.user_id.email, order.matched_user_id.email]
        # メールの件名
        subject = '【リマインダー】pairlearyからのお知らせ'
        # メールの本文
        message = 'ご希望の予約が完了しました。詳細はアプリで確認してください。'
        from_email = settings.EMAIL_HOST_USER  # 送信元のメールアドレス
        mail = EmailMessage(subject, message, from_email=from_email, bcc=bcc_list)
        mail.send()

        return redirect('mypage')
    return render(request, 'search_matching.html', context)

@login_required(login_url='/login/')
# チュートリアル画面
def tutorial(request):
    return render(request, "tutorial.html")

class Header(TemplateView):
    template_name = "header.html"

# モーダルに値を受け渡すための関数
def mypage_modal(request):
    user = request.user
    # ユーザーIDがログインしているユーザーと一致する予約情報を取得
    order_data = Orders.objects.filter(user_id_id=user)
    return render(request, 'mypage-modal.html', {'order_data': order_data})

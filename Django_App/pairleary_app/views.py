from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin  # 追加
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Orders
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password


# 新規登録
# def signupfunc(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         try:
#             user = CustomUser.objects.create_user(username, email, password)
#             # user = User.objects.create_user(username, email, password)
#             return redirect('login')
#         except IntegrityError:
#             return render(request, 'signup.html', {'error': 'このユーザーは登録済みです。'})
#     return render(request, 'signup.html')
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender_type = request.POST['gender']
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password, **{'gender_type': gender_type})
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
@login_required
def mypage(request):
    user = request.user
    # ユーザーIDがログインしているユーザーと一致する予約情報を取得
    order_data = Orders.objects.filter(user_id_id = user)
    # 画面側から送られてきた箇所をアップデートする
    if request.method == 'POST':
        try:
            if 'username' in request.POST:
                user = request.user
                print(user)
                new_username = request.POST.get('username')
                user.username = new_username
                print(user)
                user.save()
                return redirect('mypage')
            if 'email' in request.POST:
                user = request.user
                new_email = request.POST.get('email')
                user.email = new_email
                user.save()
                return redirect('mypage')
            if 'gender' in request.POST:
                user = request.user
                new_gender = request.POST.get('gender')
                user.gender_type = new_gender
                user.save()
                return redirect('mypage')
            if 'password' in request.POST:
                user = request.user
                new_password = request.POST.get('password')
                hashed_password = make_password(new_password)
                user.password = hashed_password
                user.save()
                # セッションを再認証する
                user = authenticate(username=user.username, password=new_password)
                if user is not None:
                    login(request, user)
                return redirect('mypage')
        except IntegrityError:
            return render(request, 'mypage.html', {'error': '問題が発生しました。リロードしてください。'})
        
    return render(request, 'mypage.html', {'order_data': order_data,})

# マッチング新規予約
def create_order(request):
    if request.method == 'POST':
        try:
            obj = Orders.objects.create(                
                order_date=request.POST['date'],  # マッチング日付
                order_time_range_type=request.POST['time'],  # マッチング時間帯
                category=request.POST['purpose'],  # 目的（カテゴリ）
                hope_gender_type=request.POST['gender'],  # 希望する相手の性別
                comment=request.POST['comment'],  # コメント
                user_id_id=request.user.id  # user_id
                )
        # except ValueError:
        #     return render(request, 'create_order.html', {'error_K': '全ての'})
        except Exception:
            return render(request, 'create_order.html', {'error': '全ての希望条件を選択してください'})
        else:
            return redirect('search_matching')
    else:
        return render(request, 'create_order.html')

# ログインしているユーザーにのみ表示される
# @login_required(login_url='/login/')
# マッチング検索機能
def search_matching(request):
    if request.method == "POST":
        #フォームから入力された条件を受け取る
        category = request.POST.get("purpose")
        gender = request.POST.get("gender")
        #ordersテーブルからカテゴリがcategory、性別がどちらでもOK、マッチング相手がいないデータを取得
        if gender == 'どちらでもOK':
            orders = Orders.objects.filter(
                category=category, 
                matched_user_id__isnull=True, 
                ).exclude(user_id=request.user).select_related('user_id')
        else:
            #ordersテーブルからカテゴリがcategory、性別がgender、マッチング相手がいないデータを取得
            orders = Orders.objects.filter(
                category=category, 
                matched_user_id__isnull=True, 
                user_id__gender_type=gender
                ).exclude(user_id=request.user).select_related('user_id')
        if orders:
            context = {'orders': orders}
        else:
            context = {'error_message': '条件に一致するデータがありません'}

    else:
        context = {}
    
    # 申し込みボタンが押された場合
    if request.method == "POST" and 'matching_button' in request.POST:
        order_id = request.POST.get('order_id')
        order = Orders.objects.get(pk=order_id)
        order.matched_user_id = request.user

        order.save()
        # メール送信処理
        recipient_list = [order.user_id.email, order.matched_user_id.email]        
        # メールの件名
        subject = '【リマインダー】pairlearyからのお知らせ'
        # メールの本文
        message = 'ご希望の予約が完了しました。詳細はアプリで確認してください。'
        from_email = settings.EMAIL_HOST_USER  # 送信元のメールアドレス

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect('mypage')
    
    return render(request, 'search_matching.html', context)

class Tutorial(TemplateView):
    template_name = "tutorial.html"

class Header(TemplateView):
    template_name = "header.html"

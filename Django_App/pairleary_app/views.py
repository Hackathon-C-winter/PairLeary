from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin  # 追加
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Orders

# 新規登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = CustomUser.objects.create_user(username, email, password)
            # user = User.objects.create_user(username, email, password)
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
    return render(request, 'mypage.html', {'order_data': order_data,})

# マッチング新規予約
def create_order(request):

    if request.method == 'POST':

        obj = Orders.objects.create(
            # マッチング日付
            order_date = request.POST['date'],
            # マッチング時間帯
            order_time_range_type = request.POST['time'],
            # 目的（カテゴリ）
            category = request.POST['purpose'],
            # 希望する相手の性別
            hope_gender_type = request.POST['gender'],
            # コメント
            comment = request.POST['comment'],
            # user_id
            user_id_id = request.user.id
            )

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
    return render(request, 'search_matching.html', context)

class Tutorial(TemplateView):
    template_name = "tutorial.html"

class Header(TemplateView):
    template_name = "header.html"
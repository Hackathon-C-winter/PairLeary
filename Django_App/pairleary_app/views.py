from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Orders

# 新規登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
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
            # return render(request, 'tutorial.html', {})
            return  redirect('signup')
    return render(request, 'login.html', {})


class MyPage(TemplateView):
    template_name = "mypage.html"

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

class SearchMatching(TemplateView):
    template_name = "search_matching.html"

class Tutorial(TemplateView):
    template_name = "tutorial.html"

class Header(TemplateView):
    template_name = "header.html"


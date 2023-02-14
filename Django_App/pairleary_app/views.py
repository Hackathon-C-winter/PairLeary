from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import CustomUser


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = CustomUser.objects.create_user(username, email, password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録済みです。'})
    return render(request, 'signup.html')


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


class MyPage(TemplateView):
    template_name = "mypage.html"

class CreateOrder(TemplateView):
    template_name = "create_order.html"

class SearchMatching(TemplateView):
    template_name = "search_matching.html"

class Tutorial(TemplateView):
    template_name = "tutorial.html"

class Header(TemplateView):
    template_name = "header.html"


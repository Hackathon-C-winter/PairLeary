from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Orders


# Create your views here.

# class SignupUser(TemplateView):
#     template_name = "signup.html"
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            # return render(request, 'login.html', {'some': 100})
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録済みです。'})
    return render(request, 'signup.html')


# class LoginUser(TemplateView):
#     template_name = "login.html"
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


# class MyPage(TemplateView):
#     template_name = "mypage.html"

class MyPage(View):
    def get(self, request, *args, **kwargs):
        order_data = Orders.objects.all()
        user_data = User.objects.all()

        return render(request, 'mypage.html', {
            'order_data': order_data,
            'user_data': user_data,
        })

class CreateOrder(TemplateView):
    template_name = "create_order.html"

class SearchMatching(TemplateView):
    template_name = "search_matching.html"

class Tutorial(TemplateView):
    template_name = "tutorial.html"

class Header(TemplateView):
    template_name = "header.html"


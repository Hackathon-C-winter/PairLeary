from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SignupUser(TemplateView):
    template_name = "signup.html"

class LoginUser(TemplateView):
    template_name = "login.html"

class MyPage(TemplateView):
    template_name = "mypage.html"

class CreateOrder(TemplateView):
    template_name = "create_order.html"

class SearchMatting(TemplateView):
    template_name = "search_matting.html"

class Tutorial(TemplateView):
    template_name = "tutorial.html"
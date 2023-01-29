from django.urls import path
from .views import login,mypage


urlpatterns = [
    path('login/', login, name='login'),
    path('mypage/', mypage, name='mypage'),

]

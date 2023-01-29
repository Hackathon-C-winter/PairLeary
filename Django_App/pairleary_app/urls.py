from django.urls import path
from .views import login, mypage, signupfunc


urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', login, name='login'),
    path('mypage/', mypage, name='mypage'),
    
]

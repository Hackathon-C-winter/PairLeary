from django.urls import path
from .views import loginfunc, mypage, create_order, search_matching,\
      signupfunc, tutorial, Header, logoutfunc


urlpatterns = [
    path('', loginfunc, name='login'),
    path('login/', loginfunc, name='login'),
    path('mypage/', mypage, name='mypage'),
    path('order/', create_order, name='create_order'),
    path('matching/', search_matching, name='search_matching'),
    path('signup/', signupfunc, name='signup'),
    path('tutorial/', tutorial, name='tutorial'),
    path('header/', Header.as_view(), name='header'),
    path('logout/', logoutfunc, name='logout')
]

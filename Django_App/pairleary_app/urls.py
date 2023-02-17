from django.urls import path
from .views import loginfunc, MyPage, create_order, search_matching,\
      signupfunc, Tutorial, Header, logoutfunc


urlpatterns = [
    # path('signup/', signupfunc, name='signup'),
    # path('login/', LoginUser.as_view(), name='login'),
    path('login/', loginfunc, name='login'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    path('order/', create_order, name='create_order'),
    # path('matching/', SearchMatching.as_view(), name='search_matching'),
    path('matching/', search_matching, name='search_matching'),
    # path('signup/', SignupUser.as_view(), name='signup'),
    path('signup/', signupfunc, name='signup'),
    path('tutorial/', Tutorial.as_view(), name='tutorial'),
    path('header/', Header.as_view(), name='header'),
    path('logout/', logoutfunc, name='logout')
]

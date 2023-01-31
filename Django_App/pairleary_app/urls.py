from django.urls import path
from .views import LoginUser, MyPage, CreateOrder, SearchMatting, SignupUser, Tutorial, Header


urlpatterns = [
    # path('signup/', signupfunc, name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    path('order/', CreateOrder.as_view(), name='create_order'),
    path('matting/', SearchMatting.as_view(), name='search_matting'),
    path('signup/', SignupUser.as_view(), name='signup'),
    path('tutorial/', Tutorial.as_view(), name='tutorial'),
    path('header/', Header.as_view(), name='header'),


]

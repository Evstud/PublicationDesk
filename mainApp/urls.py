from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import NoticeList, ResponseList, ResponseCreateView, NoticeCreateView, NoticeDetailView, BaseRegisterView, IndexView, SignupEndView, NoticeDeleteView

urlpatterns = [
    path('', NoticeList.as_view(), name='main'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('response_create/', ResponseCreateView.as_view(), name='response_create'),
    path('notice_create/', NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>_notice_detail/', NoticeDetailView.as_view(), name='notice_detail'),
    path('<int:pk>_notice_delete/', NoticeDeleteView.as_view(), name='notice_delete'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('users_page/', IndexView.as_view(template_name='login/users_page.html'), name='users_page'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='login/signup.html'), name='signup'),
    path('signup_end/', SignupEndView.as_view(template_name='login/signup_end.html'), name='signup_end'),
]

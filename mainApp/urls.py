from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import NoticeList, ResponseList, ResponseCreateView, NoticeCreateView, NoticeDetailView, BaseRegisterView, IndexView, SignupEndView, NoticeDeleteView, NoticeUpdateView, ResponseCreatedView, admit_response, ResponseDeleteView

urlpatterns = [
    path('', NoticeList.as_view(), name='main'),
    path('users_page/responses/', ResponseList.as_view(), name='responses'),
    path('<int:pk>/response_create/', ResponseCreateView.as_view(), name='response_create'),
    path('<int:pk>/response_created/', ResponseCreatedView.as_view(), name='response_created'),
    path('<int:pk>/response_delete/', ResponseDeleteView.as_view(), name='response_delete'),
    path('users_page/responses/<int:pk>/admit_response/', admit_response, name='admit_response'),
    path('notice_create/', NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>/notice_update/', NoticeUpdateView.as_view(), name='notice_update'),
    path('<int:pk>/notice_detail/', NoticeDetailView.as_view(), name='notice_detail'),
    path('<int:pk>/notice_delete/', NoticeDeleteView.as_view(), name='notice_delete'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('users_page/', IndexView.as_view(template_name='login/users_page.html'), name='users_page'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='login/signup.html'), name='signup'),
    path('signup_end/', SignupEndView.as_view(template_name='login/signup_end.html'), name='signup_end'),
]

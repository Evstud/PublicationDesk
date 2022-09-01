from django.urls import path
from .views import NoticeList, ResponseList, ResponseCreateView, NoticeCreateView, NoticeDetailView

urlpatterns = [
    path('', NoticeList.as_view(), name='main'),
    path('responses/', ResponseList.as_view(), name='responses'),
    path('response_create/', ResponseCreateView.as_view(), name='response_create'),
    path('notice_create/', NoticeCreateView.as_view(), name='notice_create'),
    path('<int:pk>_notice_detail/', NoticeDetailView.as_view(), name='notice_detail'),
]

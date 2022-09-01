from django.forms import ModelForm
from .models import Notice, Response


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = ['noticeTitle', 'noticeText', 'noticeCategory']


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['responseText']

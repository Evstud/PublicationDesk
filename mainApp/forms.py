from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Notice, Response


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = ['noticeTitle', 'noticeText', 'noticeCategory']


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['responseText']


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2', )


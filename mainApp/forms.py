from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
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
    email = models.EmailField(unique=True)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2', )


class ActivationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
    code_inp = forms.CharField(
        required=True,
        max_length=5,
        label='Код подтверждения',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Введите код!', 'max_length': 'Максимальное количество символов - 5'},
    )


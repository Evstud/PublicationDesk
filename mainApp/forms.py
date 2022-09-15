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

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['noticeTitle'].label = 'Заголовок объявления'
        self.fields['noticeText'].label = 'Текст объявления'
        self.fields['noticeCategory'].label = 'Категория объявления'

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['responseText']

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['responseText'].label = 'Текст отклика'


class BaseRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2'
                  )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя'
        self.fields['username'].help_text = 'Необходимо заполнить это поле. 150 или менее символов. Допустимы буквы,' \
                                        ' цифры и @/./+/-/_'
        self.fields['username'].error_messages = {'required': 'Необходимо заполнить это поле.'}
        self.fields['email'].label = 'Email'
        self.fields['email'].error_messages = {'required': 'Необходимо заполнить это поле.'}
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].help_text = '<ul><li>Ваш пароль не может быть схож с персональной информацией.</li>' \
                                             '<li>Ваш пароль должен содержать не менее 8 символов.</li>' \
                                             '<li>Ваш пароль не может состоять только из цифр.</li>'
        self.fields['password1'].error_messages = {'required': 'Необходимо заполнить это поле.'}
        self.fields['password2'].label = 'Пароль еще раз'
        self.fields['password2'].help_text = 'Введите пароль еще раз для верификации'
        self.fields['password2'].error_messages = {'required': 'Необходимо заполнить это поле'}

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', "Эта почта уже зарегистрирована")
        return cleaned_data


class ActivationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
    code_inp = forms.CharField(
        required=True,
        max_length=5,
        label='Код подтверждения',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Введите код!', 'max_length': 'Максимальное количество символов - 5'},
    )


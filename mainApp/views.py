from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Notice, Response, OneTimeCode
from .forms import NoticeForm, ResponseForm, BaseRegisterForm, ActivationForm



class NoticeList(ListView):
    model = Notice
    template_name = 'notices.html'
    context_object_name = 'notices'


class ResponseList(ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'


class NoticeDetailView(DetailView):
    template_name = 'notice_detail.html'
    queryset = Notice.objects.all()


class NoticeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notice_create.html'
    form_class = NoticeForm
    success_url = ''


class ResponseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm
    success_url = ''


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users_page.html'
    success_url = 'users_page.html'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/notice_desk/signup_end/'


class SignupEndView(FormView):
    template_name = 'signup_end.html'
    form_class = ActivationForm
    success_url = '/notice_desk/'

    # def get_object(self):
    #     return User.objects.get(pk=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user_input_code = int(request.POST.get('code_inp'))
        print(request.user)
        user_created_code = OneTimeCode.objects.get(user__username=request.POST.get('username'))
        print(user_created_code)
        print(type(user_created_code.code))
        print(type(user_input_code))
        if user_input_code == user_created_code.code:
            current_user = User.objects.get(username=request.user.username)
            current_user.is_active = True
            current_user.save()
            print('OK!!!')
            return redirect('/notice_desk/')
        else:
            print('Not yet!!!')
            return redirect('/notice_desk/signup_end')

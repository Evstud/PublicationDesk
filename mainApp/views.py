from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import date, timedelta

from .models import Notice, Response, OneTimeCode
from .forms import NoticeForm, ResponseForm, BaseRegisterForm, ActivationForm
from .filters import ResponseFilter


class NoticeList(ListView):
    model = Notice
    template_name = 'notices.html'
    context_object_name = 'notices'
    queryset = Notice.objects.all().order_by('-noticeDate')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_user'] = self.request.user
        print(self.request.user)
        return context


class NoticeDetailView(DetailView):
    template_name = 'notice_detail.html'
    context_object_name = 'notice'
    queryset = Notice.objects.all()


class NoticeDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('mainApp.delete_notice',)
    template_name = 'notice_delete.html'
    queryset = Notice.objects.all()
    success_url = '/notice_desk/'


class NoticeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'notice_create.html'
    form_class = NoticeForm

    def post(self, request, *args, **kwargs):
        author_req = request.user
        notice_author = User.objects.get(id=author_req.id)
        notice = Notice(
            noticeAuthor = notice_author,
            noticeTitle = request.POST['noticeTitle'],
            noticeText = request.POST['noticeText'],
            noticeCategory = request.POST['noticeCategory'],
        )
        notice.save()
        return redirect('/notice_desk/')


class NoticeUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('mainApp.change_notice', )
    template_name = 'notice_create.html'
    form_class = NoticeForm
    success_url = '/notice_desk/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Notice.objects.get(pk=id)


class ResponseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm

    def post(self, request, *args, **kwargs):
        response_author = request.user
        response_notice = Notice.objects.get(id=request.resolver_match.kwargs.get('pk'))
        response = Response(
            responseAuthor = response_author,
            responseNotice = response_notice,
            responseText = request.POST['responseText'],
        )
        response.save()
        return redirect('response_created', pk=response.id)


class ResponseCreatedView(LoginRequiredMixin, DetailView):
    template_name = 'response_created.html'
    context_object_name = 'response'
    queryset = Response.objects.all()


class ResponseList(ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'
    # queryset = Response.objects.all().filter(responseNotice__noticeAuthor=self.request.user)

    def notices_for_filter(request):
        print(request)
        notice_author = request.user
        return notice_author.notice_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_user'] = self.request.user
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        context['copyright'] = 'Невозможно отобразить отклики на объявления, опубликованные другим автором'
        if self.request.GET:
            notice = Notice.objects.all().get(id=self.request.GET['responseNotice'])
            context['noticeAuthorCon'] = notice.noticeAuthor
        return context


class ResponseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('mainApp.delete_response',)
    template_name = 'response_delete.html'
    queryset = Response.objects.all()
    success_url = '/notice_desk/users_page/responses/'


def email_sender(list_of_readers, list_of_notices):
   for subscriber in list_of_readers:
        html_content = render_to_string(
            'notices_one_week.html',
            {
                'notices': list_of_notices,
                'subscribername': subscriber.username,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'News by week',
            body='News',
            from_email='EvgStud@yandex.ru',
            to=[subscriber.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def send_news(*args, **kwargs):
    startdate = date.today()
    enddate = startdate - timedelta(days=7)
    list_of_notices = Notice.objects.filter(noticeDate__range=[enddate, startdate])
    list_of_readers = User.objects.all()
    email_sender(list_of_readers, list_of_notices)
    return redirect('/notice_desk/')


@login_required
def admit_response(request, pk):
    user = request.user
    response_to_admit = Response.objects.get(id=pk)
    response_to_admit.responseAdmission = True
    response_to_admit.save()

    html_content = render_to_string(
            'response_admitted.html',
            {
                'username': response_to_admit.responseAuthor.username,
                'response': response_to_admit,
            }
        )

    msg = EmailMultiAlternatives(
            subject=f'Отклик принят',
            body='Hi!',
            from_email='EvgStud@yandex.ru',
            to=[response_to_admit.responseAuthor.email]
        )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return redirect('/notice_desk/users_page/responses/')


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

    def post(self, request, *args, **kwargs):
        user_input_code = int(request.POST.get('code_inp'))
        user_created_code = OneTimeCode.objects.get(user__username=request.POST.get('username'))
        if user_input_code == user_created_code.code:
            current_user = User.objects.get(username=request.POST.get('username'))
            current_user.is_active = True
            current_user.save()
            return redirect('/notice_desk/')
        else:
            return redirect('/notice_desk/signup_end')




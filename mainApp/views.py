from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notice, Response
from .forms import NoticeForm, ResponseForm



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

from django.views.generic import ListView, DetailView, CreateView
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


class NoticeCreateView(CreateView):
    template_name = 'notice_create.html'
    form_class = NoticeForm
    success_url = '/notices/'


class ResponseCreateView(CreateView):
    template_name = 'response_create.html'
    form_class = ResponseForm
    success_url = '/notices/'

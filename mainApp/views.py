from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Notice, Response, OneTimeCode
from .forms import NoticeForm, ResponseForm, BaseRegisterForm, ActivationForm



class NoticeList(ListView):
    model = Notice
    template_name = 'notices.html'
    context_object_name = 'notices'
    queryset = Notice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['post_categories'] = PostCategory.objects.all()
        context['author_user'] = self.request.user
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


class ResponseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'response_created.html'
    context_object_name = 'response'
    queryset = Response.objects.all()

    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['response_notice'] = Notice.objects.get(id=Response.objects.get)
    #     return context

class ResponseList(ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'


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
        user_input_code = int(request.POST.get('code_inp'))
        user_created_code = OneTimeCode.objects.get(user__username=request.POST.get('username'))
        if user_input_code == user_created_code.code:
            current_user = User.objects.get(username=request.POST.get('username'))
            current_user.is_active = True
            current_user.save()
            return redirect('/notice_desk/')
        else:
            return redirect('/notice_desk/signup_end')

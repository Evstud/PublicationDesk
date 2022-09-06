from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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








#
# # for email code
# def generate_code():
#     random.seed()
#     return str(random.randint(10000, 99999))

#
# def register(request):
#     if not request.user.is_authenticated:
#         if request.POST:
#             form = RegistrationForm(request.POST or None)
#             if form.is_valid():
#                 form.save()
#                 username = form.cleaned_data.get('username')
#                 my_password1 = form.celaned_data.get('password1')
#                 code = generate_code()
#                 message = code
#                 user = authenticate(username=username, password=my_password1)
#                 send_mail('код подтверждения', message, settings.EMAIL_HOST_USER,
#                           ['test@mail.ru'],
#                           fail_silently=False)
#                 if user and user.is_active:
#                     login(request, user)
#                     return redirect('/personalArea/')
#                 else:
#                     form.add_error(None, "Unknown or disabled account")
#                     return render(request, 'registration/register.html', {'form': form})
#             else:
#                 return render(request, 'registration/register.html', {'form': form})
#         else:
#             return render(request, 'registration/register.html', {'form': form})
#             RegistrationForm()
#     else:
#         return redirect('/personalArea/')
#
# def endreg(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             code_use = form.cleaned_data.get('key')
#             user = User.objects.get(code=code_use)
#             user.is_active = True
#             user.save()
#         else:
#             form = NameForm1()

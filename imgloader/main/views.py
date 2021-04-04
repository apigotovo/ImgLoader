from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import AnonymousRequiredMixin, AjaxResponseMixin, JSONResponseMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView
from .forms import RegistrationForm, ImgUploadForm
from .models import MediaImg, ImgHistory


# Вход
class CustomLoginView(AnonymousRequiredMixin, LoginView):
    authenticated_redirect_url = reverse_lazy('index')


# Регистрация
class UserRegistration(AnonymousRequiredMixin, FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "registration/create_user.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Загрузка файлов
class ImgUpload(LoginRequiredMixin, JSONResponseMixin, AjaxResponseMixin, CreateView):
    form_class = ImgUploadForm
    template_name = 'main/upload_img.html'
    success_url = reverse_lazy('index')

    def post_ajax(self, request, *args, **kwargs):
        form = ImgUploadForm(request.POST, request.FILES)
        form.instance.created_at = datetime.now()
        form.instance.author = self.request.user
        if form.is_valid():
            form.save()
            return HttpResponse('Изображение успешно загружено!')
        else:
            return HttpResponse('Файл не загружен! Максимально допустимый размер файла 2Мб')


# Обновление файла
class ImgUpdate(LoginRequiredMixin, UpdateView):
    form_class = ImgUploadForm
    template_name = 'main/update_img.html'
    success_url = reverse_lazy('account')
    queryset = MediaImg.objects.all()


# Личный кабинет
class Account(LoginRequiredMixin, ListView):
    template_name = 'main/account.html'
    context_object_name = 'img_list'
    paginate_by = 100

    def get_queryset(self):
        return MediaImg.objects.filter(author=self.request.user).order_by('created_at').reverse()


# История изменений
class HistoryImg(LoginRequiredMixin, ListView):
    template_name = 'main/history.html'
    context_object_name = 'img_history'
    paginate_by = 100

    def get_queryset(self):
        return ImgHistory.objects.filter(img=self.kwargs['pk']).order_by('updated_at').reverse()

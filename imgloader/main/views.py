import os
from datetime import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import AnonymousRequiredMixin, AjaxResponseMixin, JSONResponseMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import RegistrationForm, ImgUploadForm


def logger(message, mr_data):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path = os.path.join(settings.BASE_DIR, f'error_log/{now}_{message}.txt')
    file = open(path, 'w')
    file.write(str(mr_data))
    file.close()


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

    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post_ajax(self, request, *args, **kwargs):
        logger('a', request.POST)
        form = ImgUploadForm(request.POST)
        context = {}
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['fail'] = True
        context['form'] = ImgUploadForm(initial={'created_at': datetime.now(), 'author': request.user})
        return render(request, 'main/upload_img.html', context)


def img_upload(request):
    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            form.save()
            context['success'] = True
        else:
            context['fail'] = True
        context['form'] = ImgUploadForm(initial={'created_at': datetime.now(), 'author': request.user})
        return render(request, 'main/upload_img.html', context)
    else:
        form = ImgUploadForm(initial={'created_at': datetime.now(), 'author': request.user})
    context = {'form': form}
    return render(request, 'main/upload_img.html', context)

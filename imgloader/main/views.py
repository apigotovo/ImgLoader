from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import AnonymousRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import RegistrationForm, ImgUploadForm


class CustomLoginView(AnonymousRequiredMixin, LoginView):
    authenticated_redirect_url = reverse_lazy('index')


class UserRegistration(AnonymousRequiredMixin, FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "registration/create_user.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ImgUpload(LoginRequiredMixin, CreateView):
    form_class = ImgUploadForm
    template_name = 'main/upload_img.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        form.instance.author = self.request.user
        return super().form_valid(form)


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

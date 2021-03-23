from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegistrationForm


class UserRegistration(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "registration/create_user.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)






from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import MediaImg


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Поле email обязательно к заполнению')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ImgUploadForm(forms.ModelForm):
    class Meta:
        model = MediaImg
        fields = ['img', ]

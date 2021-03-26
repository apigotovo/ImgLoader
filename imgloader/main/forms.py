from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .const import MAX_UPLOAD_SIZE
from .models import MediaImg


def file_size_validator(value):
    limit = MAX_UPLOAD_SIZE
    if value.size > limit:
        raise ValidationError('Максимально допустимый размер файла 2Мб')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Поле email обязательно к заполнению')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ImgUploadForm(forms.ModelForm):

    img = forms.ImageField(validators=[file_size_validator], label='Загрузить изображение')

    class Meta:
        model = MediaImg
        fields = ['img', ]









from django.contrib.auth.models import User
from django.db import models


class MediaImg(models.Model):

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name_plural = 'изображения'
        verbose_name = 'изображение'

    img = models.ImageField(verbose_name='изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    created_at = models.DateTimeField(verbose_name='дата/время загрузки файла')


class ImgHistory(models.Model):

    def __str__(self):
        return str(self.updated_at)

    class Meta:
        verbose_name_plural = 'история изменений'
        verbose_name = 'обновление'

    updated_at = models.DateTimeField(verbose_name='дата/время изменения')
    img = models.ForeignKey(MediaImg, on_delete=models.CASCADE, verbose_name='изображение')

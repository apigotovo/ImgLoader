# Generated by Django 3.1.7 on 2021-03-23 22:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', validators=[django.core.validators.validate_image_file_extension], verbose_name='изображение')),
                ('created_at', models.DateTimeField(verbose_name='дата/время загрузки файла')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
            },
        ),
    ]

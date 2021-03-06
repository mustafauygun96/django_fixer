# Generated by Django 2.0.6 on 2018-07-09 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adiniz', models.CharField(max_length=50, verbose_name='Kullanıcı Adınız:')),
                ('soyadiniz', models.CharField(max_length=50, verbose_name='Parolanız:')),
                ('phone_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Lütfen Telefon Numaranızı Başında 0 olmadan giriniz.', regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefon Numaranız:')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('password', models.CharField(max_length=50, verbose_name='Parolanız:')),
                ('confirm_password', models.CharField(max_length=50, verbose_name='Parolanızı Tekrar Giriniz:')),
                ('d_tarih', models.DateField(verbose_name='Doğum Tarihiniz:')),
                ('aciklama', models.CharField(max_length=100, verbose_name='Kısaca Kayıt Nedeninizi Açıklayınız.')),
            ],
        ),
    ]

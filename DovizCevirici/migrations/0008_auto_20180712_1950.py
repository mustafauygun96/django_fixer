# Generated by Django 2.0.6 on 2018-07-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DovizCevirici', '0007_auto_20180712_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevirilenparalar',
            name='sonuc',
            field=models.FloatField(verbose_name='Sonuç'),
        ),
    ]

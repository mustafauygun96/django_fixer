from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# Create your models here.
class Sponsorlar(models.Model):
    sponsor_ad = models.CharField(max_length=255, blank=True)
    sponsor_foto = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.sponsor_ad

    class Meta:
        verbose_name_plural = "Sponsorlar"

# Admin Panelinden gönderiyi sildiğinizde fotoğrafın da klasörden silinmesi kodu
@receiver(models.signals.post_delete, sender=Sponsorlar)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.sponsor_foto:
        if os.path.isfile(instance.sponsor_foto.path):
            os.remove(instance.sponsor_foto.path)

@receiver(models.signals.pre_save, sender=Sponsorlar)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).sponsor_foto
    except sender.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

# Admin Panelinden gönderiyi sildiğinizde fotoğrafın da klasörden silinmesi kodu bitiş

class CevirilenParalar(models.Model):
    ceviren = models.ForeignKey(User,verbose_name='Üye Adı',on_delete=models.CASCADE,null=True)
    ana_para = models.CharField(max_length=20,verbose_name='Ana Para',null=True)
    cevirilen_para = models.CharField(max_length=20,verbose_name='Çevirilen Para',null=True)
    cevirilen_miktar = models.FloatField(verbose_name='Çevirilen Miktar')
    sonuc = models.FloatField(verbose_name='Sonuç')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",null=True)

    def __str__(self):
        return '%s  (%s - %s)' % (self.ceviren, self.ana_para,self.cevirilen_para)

    class Meta:
        verbose_name_plural = "Çevirilen Paralar"
    

"""FixerDoviz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include 
from django.urls import path
from DovizCevirici import views
from django.contrib.auth import views as auth_views
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='anasayfa'),
    path('hakkimizda', views.hakkimizda,name='hakkimizda'),
    path('giris', auth_views.login,{'template_name': 'login.html'},name='login',),
    path('logout',auth_views.logout, {'next_page': '/giris'},name='login'),
    path('kayit-ol',views.kayitol,name='kayitol'),
    path('sponsorlarimiz',views.sponsorlar,name='sponsorlar'),
    path('sponsor-ekle',views.sponsorekle,name='SponsorEkle'),
    url('^', include('django.contrib.auth.urls')),
    path('dashboard',views.dashboard,name='dashboard'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

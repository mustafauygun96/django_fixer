from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,user_logged_in
from DovizCevirici.forms import SignUpForm,SponsorForm,ContactForm
from django.core.mail import EmailMessage, BadHeaderError,send_mail
import requests
from django.contrib import messages
from DovizCevirici.models import Sponsorlar,CevirilenParalar
from .decorators import check_recaptcha
from django.utils import timezone
# Create your views here.
def homepage(request):
    response = requests.get('http://data.fixer.io/api/latest?access_key=347372d046965f724a4cd7ada24cc8fb')
    geodata = response.json()
    para_birimleri = geodata['rates']
    if request.method == 'POST':
        firstCurrency = request.POST.get("firstCurrency") # USD aldık varsayalım.
        secondCurrency = request.POST.get("secondCurrency") # TRY aldık varsayalım.
        amount = request.POST.get("amount") # 15 girdik varsayalım.

        
        firstValue = para_birimleri[firstCurrency]
        secondValue = para_birimleri[secondCurrency]

        result = (secondValue / firstValue) * float(amount)
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = "%.5f" % result
        kullanici = request.user
        kaydet = CevirilenParalar.objects.create(ceviren=kullanici,ana_para=firstCurrency, cevirilen_para=secondCurrency,cevirilen_miktar=amount,sonuc="%.5f" % result,created_date=timezone.now())
        kaydet.save()
        return render(request, 'index.html', {'para_birimleri': para_birimleri,'info':currencyInfo})
    
    else:
        return render(request, 'index.html', {'para_birimleri': para_birimleri})


def hakkimizda(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid(): # site yayına alındığında bu kod eklenecek --> and request.recaptcha_is_valid
            adiniz = form.cleaned_data['adiniz']
            soyadiniz = form.cleaned_data['soyadiniz']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = "Gönderen Adı: " + adiniz + "\n" + "Gönderen Soyadı: " + soyadiniz + "\n" + "Mesaj: " + form.cleaned_data['message']
            try:
                email = EmailMessage(
                    subject,
                    message,
                    from_email +'<sender@gmail.com>',
                    ['mustafauygun981@gmail.com'],
                    headers = {'Reply-To': from_email }
                ) 
                email.send()
                messages.success(request, 'Mailiniz Başarıyla Gönderildi.')
            except BadHeaderError:
                messages.warning(request, 'Geçersiz Başlık Bulundu')
            return redirect('hakkimizda')
    return render(request, "hakkimizda.html", {'form': form})


def kayitol(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('anasayfa')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='anasayfa',redirect_field_name='erisme-yetkiniz-yok')
def sponsorekle(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sponsor Başarıyla Kaydoldu.')
            return redirect('SponsorEkle')
            
    else:
        form = SponsorForm()
    return render(request, 'sponsor_ekle.html', {
        'form': form
    })


def sponsorlar(request):
    sponsorlarimiz = Sponsorlar.objects.all()
    return render(request,'sponsorlar.html',{'sponsorlarimiz':sponsorlarimiz})

@login_required(login_url='anasayfa',redirect_field_name='erisme-yetkiniz-yok')
def dashboard(request):
    kullanici = request.user
    doviz_bilgi = CevirilenParalar.objects.filter(ceviren=kullanici)
    return render(request,'dashboard.html',{'doviz_bilgi':doviz_bilgi})
    
    


from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail 
from django.shortcuts import redirect

#listings/views.py

def contact(request):
    if request.method=='POST':
        form= ContactUsForm(request.POST) # crée une instance de notre formulaire et le remplir avec les données Posts

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message= form.cleaned_data['message'],
            from_email= form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form=ContactUsForm()
    return render(request,'listings/contact.html',{'form':form}) #Passer ce formulaire au gabarit


def band_list(request):
    bands=Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})


def band_detail(request, id): #notez le paramètre id supplémentaire
    band=Band.objects.get(id=id) #Nous insérons à jour cette ligne pour obtenir le band avec cet id 
    return render(request,'listings/band_detail.html',{'band':band}) #nous mettrons à jour cette ligne pour passer le groupe au gabarit
    

def band_update(request, id):
    band=Band.objects.get(id=id)
    if request.method=='POST':
        form=BandForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form=BandForm(instance=band)
    
    return render(request,'listings/band_update.html',{'form':form})


def email_sent(request):
    return render(request,'listings/email_sent.html')

def band_delete(request,id):
    band=Band.objects.get(id=id)

    if request.method=='POST':
        band.delete()
        return redirect('band-list')
    return render(request,'listings/band_delete.html',{'band':band})


def band_create(request):
    if request.method=='POST':
        form=BandForm(request.POST)
        if form.is_valid():
            band=form.save()
            return redirect('band-detail', band.id)

    else:
        form=BandForm()
    return render(request,'listings/band_create.html',{'form':form})
# Create your views here.

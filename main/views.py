from django.shortcuts import render,redirect
from property.models import Property, Place
from .models import Website
from django.db.models import Count, Q
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def index(request):
    property_list = Property.objects.all()
    place = Place.objects.all()
    return render(request, 'index.html', {
        'property_list': property_list,
        'place': place,
    })


def contact(request):
    info = Website.objects.last()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            redirect('/contact')
    else:
        form = ContactForm()
            
    return render(request, 'contact.html', {'form':form,
                                            'info': info,

    })


def home_search(request):
    name = request.GET.get('q', '')
    location = request.GET.get('location')
    property_search = Property.objects.filter(
        Q(place__title__icontains=location) &
        Q(title__icontains=name)
        )

    return render(request, 'search_property.html', {
        'property_search': property_search,

    })

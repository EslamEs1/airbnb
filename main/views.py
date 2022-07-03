from django.shortcuts import render,redirect
from matplotlib import category
from property.models import Property, Place
from blog.models import Post
from .models import Website
from django.db.models import Count, Q
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    property_list = Property.objects.all()[0:5]
    restaurants_list = Property.objects.filter(
        category__title='Restaurants')[0:4]
    popular_list = Property.objects.filter(
        category__title__in=['Hotel', 'villa', 'House']).order_by('?')[0:5]
    place = Place.objects.all().annotate(counts=Count('property_place'))
    post = Post.objects.all()[0:4]

    property_count = Property.objects.all().count()
    place_count = Place.objects.all().count()
    Post_count = Post.objects.all().count()
    users_count = User.objects.all().count()
    return render(request, 'index.html', {
        'property_list': property_list,
        'place': place,
        'property_count': property_count,
        'place_count': place_count,
        'users_count': users_count,
        'Post_count':Post_count,
        'Popular_list': popular_list,
        'restaurants_list':restaurants_list,
        'post':post,
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

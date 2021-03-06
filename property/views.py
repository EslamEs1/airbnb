from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import DetailView ,CreateView
from .models import Property, PropertyImage, PropertyReview
from .forms import PropertyFilter, PropertyBookForm
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django_filters.views import FilterView

# Create your views here.


class Property_list(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_hotel.html'

    

class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super(PropertyDetail, self).get_context_data(**kwargs)
        context['property_image'] = PropertyImage.objects.filter(property=self.object)
        context['property_place'] = Property.objects.filter(place=self.object.place)[0:3]
        context['property_category'] = Property.objects.filter(category=self.object.category)[0:3]
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.users = request.user
            myform.property = self.get_object()
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ')
            return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))



def property_review(request, slug):
    pro = Property.objects.get(slug=slug)
    q =request.GET.get('star')
    if q:
        if PropertyReview.objects.filter(property=pro, user=request.user).exists():
            messages.error(request, 'You have already reviewed this property')
            return redirect(reverse('property:property_detail', kwargs={'slug': slug}))
        else:
            review = PropertyReview.objects.create(
                property=pro, user=request.user, rating=q)
            return redirect(reverse('property:property_detail', kwargs={'slug': slug}))
    


class AddListing(CreateView):
    model = Property
    fields = ['image', 'title', 'description','price', 'place', 'category']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Your Listing Added Successfully')
            return redirect(reverse('property:property_list'))


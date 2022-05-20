from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView
from .models import Property, Category
from .forms import PropertyFilter
from django_filters.views import FilterView
# Create your views here.


class Property(FilterView):
    model = Property
    paginate_by = 3
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'




class PropertyDetail(DetailView):
    model = Property

# def property_detail(request, slug):
#     property = Property.objects.get(slug=slug)
#     return render(request, 'property/property_detail.html',{
#         'property':property,
#     })
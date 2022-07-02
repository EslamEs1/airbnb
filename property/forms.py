from django import forms
from .models import Property, PropertyBook, PropertyReview
import django_filters

class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = ['title','description','price','place', 'category']




class PropertyBookForm(forms.ModelForm):
    start_date = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
    end_date = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))
   
    class Meta:
        model = PropertyBook
        fields = ['start_date','end_date','guest','children']



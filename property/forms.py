from .models import Property
import django_filters

class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = ['title','description','price','place', 'category']
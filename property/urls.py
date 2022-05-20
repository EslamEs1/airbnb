from django.urls import path
from .views import Property,PropertyDetail

app_name = 'property'

urlpatterns = [ 
    path('', Property.as_view(), name='property_list'),
    # path('details/<slug:slug>',property_detail , name='property_detail'),
    path('details/<slug:slug>',PropertyDetail.as_view() , name='property_detail'),
]
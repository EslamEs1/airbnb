from django.urls import path
from .views import Property_list,PropertyDetail

app_name = 'property'

urlpatterns = [ 
    path('', Property_list.as_view(), name='property_list'),
    path('details/<slug:slug>',PropertyDetail.as_view() , name='property_detail'),
]
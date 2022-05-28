from django.urls import path
from .views import index, contact, home_search


app_name = 'main'

urlpatterns = [ 
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('search/', home_search, name='home_search'),
]
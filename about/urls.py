from django.urls import path
from .views import About_us 


app_name = 'about'

urlpatterns = [ 
    path('', About_us.as_view(), name='about'),
]
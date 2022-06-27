from django.urls import path
from .views import About_us 
from .api_views import about_api


app_name = 'about'

urlpatterns = [ 
    path('', About_us.as_view(), name='about'),

    # Api
    path('about_api/', about_api, name='about_api'),

]
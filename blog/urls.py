from django.urls import path
from .views import Article


app_name = 'blog'

urlpatterns = [ 
    path('', Article.as_view(), name='article'),
]
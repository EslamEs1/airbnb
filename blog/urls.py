from django.urls import path
from .views import Article, BlogDetail


app_name = 'blog'

urlpatterns = [ 
    path('', Article.as_view(), name='article'),
    path('details/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),

]
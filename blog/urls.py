from django.urls import path
from .views import Article, BlogDetail
from .api_views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [ 
    path('', Article.as_view(), name='article'),
    path('details/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),

    # Api
    path('post_api/', PostList.as_view(), name='post_api'),
    path('PostDetail/<int:pk>', PostDetail.as_view(), name='PostDetail_api'),



]
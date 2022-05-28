from django.shortcuts import render
from django.views.generic import ListView, DetailView
from matplotlib.style import context
from .models import Post, Category
from django.db.models import Count, Q
from django.contrib.auth.models import User


# Create your views here.

class Article(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        search = self.request.GET.get('q','')
        filters = Post.objects.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search))
        return filters

    


class BlogDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all().annotate(
            counts=Count('Category'))
        context['post'] = Post.objects.filter()[0:3]   
        return context



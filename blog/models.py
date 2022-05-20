from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse



class Post (models.Model):# Create a new Post
    author = models.ForeignKey(User, related_name='author',on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Title', unique=True)
    content = models.TextField(max_length=10000 ,verbose_name='Text')
    Category = models.ForeignKey('Category',related_name='Category', on_delete=models.CASCADE)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True, unique=True, editable=False)
    class Meta :
        ordering = ['-id']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)    
        super(Post, self).save(*args, **kwargs) 

    #Methods
    def get_absolute_url(self):
        return reverse('blog:article', args=[self.slug])

    def __str__(self):
        return self.title



class Category(models.Model):# Create a new category
    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
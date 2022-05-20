from django.contrib import admin
from .models import Post , Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    search_fields = ['title']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

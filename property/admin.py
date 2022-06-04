from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class Fk_img_product(admin.TabularInline):
    model = PropertyImage


@admin.register(Property)
class PropertyAdmin(SummernoteModelAdmin,admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    inlines = [
        Fk_img_product,
    ]
    search_fields = ['title']
    list_display = ['title', 'check_availability', 'check_rating']
    

@admin.register(PropertyBook)
class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'in_progress']

admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)


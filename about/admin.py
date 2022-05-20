from django.contrib import admin
from .models import About , FAQ
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

@admin.register(FAQ)
class About_us(admin.ModelAdmin):
    def has_add_permission(self, request):
        if FAQ.objects.count() >= 6:
          return False
        return True
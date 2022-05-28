from django.contrib import admin
from .models import Contact, Website
# Register your models here.


@admin.register(Website)
class Settings(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Website.objects.count() >= 6:
            return False
        return True
        
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('name', 'email')

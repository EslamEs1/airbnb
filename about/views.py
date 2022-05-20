from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import About,FAQ
# Create your views here.

class About_us(ListView):
    model = FAQ
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context
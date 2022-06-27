from django.shortcuts import get_object_or_404
from .serializer import About_Serializers,FAQ_Serializers
from rest_framework.response import Response
from .models import About, FAQ
from rest_framework.decorators import api_view



@api_view(('GET',))
def about_api(request):
    about_data = get_object_or_404(About)
    serialize_form = About_Serializers(about_data, context={'request': request}).data
    return Response({'about': serialize_form})

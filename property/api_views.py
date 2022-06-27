from .serilizer import Api_Serializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Property
from rest_framework.permissions import IsAuthenticated


class PropertyListApi(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = Api_Serializer
    permission_classes = [IsAuthenticated]



class PropertyDetailApi(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = Api_Serializer
    permission_classes = [IsAuthenticated]

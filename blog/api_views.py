from rest_framework.response import Response
from .serializer import PostApi
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from rest_framework.permissions import IsAuthenticated



class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi
    permission_classes = [IsAuthenticated]



class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi
    permission_classes = [IsAuthenticated]

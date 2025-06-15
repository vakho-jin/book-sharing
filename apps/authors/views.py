from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Author
from .serializers import AuthorSerializer, AuthorDetailSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
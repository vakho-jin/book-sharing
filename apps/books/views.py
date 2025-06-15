from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Genre, BookCondition
from .serializers import (
    BookListSerializer, BookDetailSerializer, BookCreateUpdateSerializer,
    GenreSerializer, BookConditionSerializer
)
from .filters import BookFilter
from .permissions import IsOwnerOrReadOnly

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.filter(is_available=True).select_related('owner', 'condition').prefetch_related('authors', 'genres')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'authors__name', 'description']
    ordering_fields = ['created_at', 'publication_year', 'title']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateUpdateSerializer
        return BookListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().select_related('owner', 'condition').prefetch_related('authors', 'genres')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return BookCreateUpdateSerializer
        return BookDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsAuthenticatedOrReadOnly()]

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookConditionListView(generics.ListAPIView):
    queryset = BookCondition.objects.all()
    serializer_class = BookConditionSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_books(request):
    books = Book.objects.filter(owner=request.user).select_related('condition').prefetch_related('authors', 'genres')
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)
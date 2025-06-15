import django_filters
from .models import Book, Genre

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    genre = django_filters.ModelMultipleChoiceFilter(
        field_name='genres',
        queryset=Genre.objects.all()
    )
    publication_year_min = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year_max = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    condition = django_filters.CharFilter(field_name='condition__name')
    location = django_filters.CharFilter(field_name='pickup_location', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_year_min', 'publication_year_max', 'condition', 'location']
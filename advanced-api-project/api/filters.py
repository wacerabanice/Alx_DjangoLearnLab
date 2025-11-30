import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # exact match: title
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')

    # contains (case-insensitive)
    title_contains = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    # publication year range
    publication_year__gte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year__lte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')

    # author by name substring
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = [
            'title', 'title_contains',
            'publication_year__gte', 'publication_year__lte',
            'author_name',
        ]

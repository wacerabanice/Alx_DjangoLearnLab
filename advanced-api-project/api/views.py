# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

class BookListView(generics.ListAPIView):
    """
    GET /api/books/?title=...&publication_year=...&author=ID
    Supports:
      - Filtering by exact fields using query params (via DjangoFilterBackend)
      - Text search via ?search=keyword (SearchFilter)
      - Ordering via ?ordering=field or ?ordering=-field (OrderingFilter)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Specify which backends to use for this view (optional if REST_FRAMEWORK defaults set)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Allow filtering by these model fields (exact match)
    filterset_fields = ['title', 'publication_year', 'author']

    # Allow search on title and author's name
    # NOTE: search will use the serializer/model fields. For related author name use 'author__name'
    search_fields = ['title', 'author__name']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['title']  # default ordering

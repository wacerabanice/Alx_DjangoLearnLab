from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, and delete actions for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

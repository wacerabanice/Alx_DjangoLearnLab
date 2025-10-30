from django.contrib import admin
from .models import Book

# Define a custom admin configuration for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('publication_year',)                     # Filter by year
    search_fields = ('title', 'author')                     # Search by title/author

# Register the Book model with the custom admin view
admin.site.register(Book, BookAdmin)

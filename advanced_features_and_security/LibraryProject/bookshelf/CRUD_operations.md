**CRUD_operations.md**
If you’d rather keep everything in one file, here’s a complete version:

# CRUD Operations for Book Model

This document demonstrates the Create, Retrieve, Update, and Delete operations for the `Book` model in the Django `bookshelf` app.

---

## Create
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

book
# <Book: 1984 by George Orwell>

## Retrive
from bookshelf.models import Book

# Retrieve all Book instances
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell>]>


# Update
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

book
# <Book: Nineteen Eighty-Four by George Orwell>


#Delete:
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
# (1, {'bookshelf.Book': 1})
# <QuerySet []>


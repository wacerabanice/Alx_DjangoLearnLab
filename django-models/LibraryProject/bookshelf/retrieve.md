 **retrieve.md**
```markdown
# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve all Book instances
Book.objects.all()


# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

book
Expected Output:

# <QuerySet [<Book: 1984 by George Orwell>]>

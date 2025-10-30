 **retrieve.md**
```markdown
# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve all Book instances
Book.objects.all()


Expected Output:

# <QuerySet [<Book: 1984 by George Orwell>]>

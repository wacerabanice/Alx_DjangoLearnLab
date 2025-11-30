from django.db import models

class Author(models.Model):
    # Stores the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)

    # Year the book was published
    publication_year = models.IntegerField()

    # Each book belongs to one author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

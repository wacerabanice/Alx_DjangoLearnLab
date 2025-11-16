from django import forms
from .models import Book, Author, Library, Librarian

# Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Include fields you want users to fill
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
        }

    # Optional: additional validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters in title")
        return title


# Author Form
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Library Form
class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'books']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'books': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

# Librarian Form
class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'library']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'library': forms.Select(attrs={'class': 'form-select'}),
        }

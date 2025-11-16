from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render
from bookshelf.models import Book
from .forms import BookForm
from bookshelf.forms import ExampleForm


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # your existing code to add a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # your existing edit logic
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('list_books')

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})


# Safe book creation
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # Validation included
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

# Safe search example
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)  # ORM handles parameterization
    return render(request, 'bookshelf/book_list.html', {'books': books})

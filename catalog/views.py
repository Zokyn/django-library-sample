from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic 

def index(request):
    # Count of some main objects
    n_books = Book.objects.all().count()
    n_instances = BookInstance.objects.all().count()

    # Available books to loan
    n_instances_available = BookInstance.objects.filter(status__exact='A').count()

    # Total of authors book 
    n_authors = Author.objects.count()

    context = {
        'n_books': n_books,
        'n_authors': n_authors,
        'n_instances': n_instances,
        'n_instances_available': n_instances_available
    }
    
    
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    queryset = Book.objects.order_by('-title')[:5]

class BookDetailView(generic.DetailView):
    model = Book
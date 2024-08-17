from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book
from .models import Library

# Create your views here.
def list_books(request):
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
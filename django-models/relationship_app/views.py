from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def register(request):
    form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
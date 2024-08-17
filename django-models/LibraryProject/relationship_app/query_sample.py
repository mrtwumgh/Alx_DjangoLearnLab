from .models import Author, Book, Library, Librarian

# Query all books by a specific author
Book.objects.filter(author='name')

# List all books in a library
Book.objects.all()

# Retrieve the librarian for a library
Librarian.objects.get(library='name')
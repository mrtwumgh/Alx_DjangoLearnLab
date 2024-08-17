from .models import Author, Book, Library, Librarian

# Query all books by a specific author
Book.objects.filter(author='author_name')

# list all books in a library
Book.objects.all()

# Retrieve the librarian for a library
Librarian.objects.get(library='library_name')
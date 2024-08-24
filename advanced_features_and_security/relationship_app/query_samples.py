from .models import Author, Book, Library, Librarian

# Query all books by a specific author
Author.objects.get(name=author_name)

# list all books in a library
Library.objects.get(name=library_name)

books.all()

# Retrieve the librarian for a library
Librarian.objects.get(library='library_name')

objects.filter(author=author)
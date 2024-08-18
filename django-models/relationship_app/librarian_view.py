from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


@user_passes_test(is_admin)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
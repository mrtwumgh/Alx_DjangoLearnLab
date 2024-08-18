from django.urls import path
from .views import list_books, LibraryDetailView
from relationship_app import views
from django.contrib.auth import views as auth_views
from librarian_view import librarian_view
from member_view import member_view

urlpatterns = [
    path('list_book/', list_books, name='list_books'),
    path('library_detail/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html', name='logout')),
    path('register/', views.register, name='register'),
    path('admin/',  views.admin_view, name='admin' ),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book', views.delete_book, name='delete_book')
]
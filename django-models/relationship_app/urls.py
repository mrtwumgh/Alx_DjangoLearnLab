from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list_book/', list_books, name='list_books'),
    path('library_detail/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html', name='logout'))
]
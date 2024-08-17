from django.urls import path
from relationship_app import views

urlpatterns = [
    path('list_book/', views.list_books, name='list_books'),
    path('library_detail/', views.LibraryDetail.as_view(), name='library_detail')
]
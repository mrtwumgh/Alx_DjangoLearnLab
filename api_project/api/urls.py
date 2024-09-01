from django.urls import path
from api import views


urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
]
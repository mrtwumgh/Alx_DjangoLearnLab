from django.shortcuts import render
from .models import Book
from rest_framework import generics, viewsets
from .serializers import BookSerializer



class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
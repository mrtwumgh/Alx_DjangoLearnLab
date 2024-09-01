from django.shortcuts import render
from api.models import Book
from rest_framework.generics import ListAPIView
from api.serializers import BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
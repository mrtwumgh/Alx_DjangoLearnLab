from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > date.today():
            raise serializers.ValidationError("The publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Author
        fields = ['id', 'name', 'book']
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=32)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
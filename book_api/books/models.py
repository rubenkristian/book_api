from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    date_created = models.DateTimeField('date created')

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_date_release = models.DateField('date release')
    date_created = models.DateTimeField('date created')
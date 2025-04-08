from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.group})"

from django.db import models

from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return self.title

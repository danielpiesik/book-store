from isbn_field import ISBNField

from django.db import models

from utils.nationalities import NATIONALITIES
from utils.genres import GENRES


class Book(models.Model):

    authors = models.ManyToManyField(
        'authors.Author',
        related_name='books',
    )
    title = models.CharField(max_length=512)
    length = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=64, choices=GENRES)
    isbn = ISBNField(unique=True)
    language = models.CharField(max_length=2, choices=NATIONALITIES)

    def __str__(self):
        return f'{self.title}'

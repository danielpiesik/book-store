from django.db import models

from isbn_field import ISBNField
from languages.fields import LanguageField


class Book(models.Model):

    FICTION = 'fiction'
    NOVEL = 'novel'
    FANTASY = 'fantasy'
    THRILLER = 'thriller'
    ROMANCE = 'romance'
    CRIME = 'crime'
    KIDS = 'kids'
    GENRES = (
        (FICTION, 'fiction'),
        (NOVEL, 'novel'),
        (FANTASY, 'fantasy'),
        (THRILLER, 'thriller'),
        (ROMANCE, 'romance'),
        (CRIME, 'crime'),
        (KIDS, 'kids'),
    )

    authors = models.ManyToManyField('authors.Author')
    title = models.CharField(max_length=512)
    length = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=64, choices=GENRES)
    isbn = ISBNField()
    language = LanguageField()

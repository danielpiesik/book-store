from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'authors',
            'title',
            'length',
            'price',
            'genre',
            'isbn',
            'language',
        )

from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'books',
            'buyer',
            'price',
            'shipping_date',
            'order_date',
        )
        read_only_fields = ('buyer', 'price', 'shipping_date', 'order_date')

    def create(self, validated_data):
        books = validated_data.pop('books', [])
        validated_data['price'] = sum(book.price for book in books)
        instance = Order.objects.create(**validated_data)
        instance.books.add(*books)
        return instance

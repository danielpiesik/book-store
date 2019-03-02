from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'birthday',
            'nationality',
            'age',
        )
        read_only_fields = ('age',)
        extra_kwargs = {'birthday': {'write_only': True}}

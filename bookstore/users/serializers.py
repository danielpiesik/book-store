from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'date_joined',
        )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('last_login', 'date_joined')

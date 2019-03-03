from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'username',
            'first_name',
            'last_name',
            'role',
            'date_joined',
            'last_login',
        )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('last_login', 'date_joined')

    def create(self, validated_data):
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = validated_data['role'].name == 'admin'
        return User.objects.create_user(**validated_data)

from django.contrib.auth.models import Group

from rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from users.models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'role',
        )
        read_only_fields = fields


class UserLoginSerializer(LoginSerializer):
    email = None


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, request):
        self.validated_data['role'] = Group.objects.get(name='buyer')
        return User.objects.create_user(**self.validated_data)

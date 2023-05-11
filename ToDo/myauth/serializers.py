from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = self.validated_data['username']
        instance.email = self.validated_data['email']
        instance.is_superuser = self.validated_data['is_superuser']
        password = validated_data.pop('password')
        instance.set_password(password)

        instance.save()
        return instance
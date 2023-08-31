from rest_framework import serializers
from django.contrib.auth.models import User

class AdminSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class Userserializer(serializers.Serializer):
    class Meta:
        model:User
        fields:'__all__'
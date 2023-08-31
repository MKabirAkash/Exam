from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employees
from .models import Gadgets

class AdminSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class Userserializer(serializers.Serializer):
    class Meta:
        model=User
        fields='__all__'

class Employeeserializer(serializers.Serializer):
    class Meta:
        model=Employees
        fields='__all__'


class Gadgetserializer(serializers.Serializer):
    class Meta:
        model=Gadgets
        fields='__all__'
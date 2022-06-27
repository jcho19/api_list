from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Api

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    apis = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'apis')

class ApiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Api
        fields = ('id', 'name', 'website', 'description', 'category', 'owner')


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    apis = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'categories', 'apis')

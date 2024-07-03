from rest_framework import serializers
from .models import post

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'title', 'content', 'created']

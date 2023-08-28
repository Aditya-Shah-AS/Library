from rest_framework import serializers
 
# import model from models.py
from .models import Book
 
# Create a model serializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Book
        fields=('title','subtitle','author','isbn')

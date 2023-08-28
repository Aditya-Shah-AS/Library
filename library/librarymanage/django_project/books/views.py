from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .Serialization import BookSerializer
# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Book.objects.all() 
    # specify serializer to be used
    serializer_class = BookSerializer

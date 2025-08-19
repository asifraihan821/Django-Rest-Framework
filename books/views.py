from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.serializers import BookSerializer
from books.models import Book
from rest_framework import status
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet   
from rest_framework import permissions

# Create your views here.
   

class BookViewSet(ModelViewSet):

    """for viewing also other functionalities to books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


  
    

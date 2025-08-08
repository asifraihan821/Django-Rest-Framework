from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books.serializers import BookSerializer
from books.models import Book
from rest_framework import status

# Create your views here.

@api_view(['GET','POST','DELETE'])
def books(request,pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view()
def all_books(request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
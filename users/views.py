from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Member,Author
from users.serializers import AuthorSerializer,MemberSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view()
def view_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many = True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def view_specific_author(request,pk):
    if request.method== 'GET':
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        author = get_object_or_404(Author, pk=pk) 
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view()
def view_members(request):
    members= Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
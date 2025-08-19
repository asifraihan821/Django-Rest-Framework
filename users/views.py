from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import Member,Author
from users import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions


# Create your views here.


class AllAuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer



class AllMembersViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]

from django.shortcuts import render
from borrow_records import serializers
from borrow_records import models
from rest_framework.viewsets import ModelViewSet



# Create your views here.

class AllBorrowRecordsViewSet(ModelViewSet):
    queryset = models.BorrowRecord.objects.all()
    serializer_class = serializers.BorrowRecordSerializer
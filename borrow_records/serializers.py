from rest_framework import serializers
from borrow_records import models as borrowModels



class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrowModels.BorrowRecord
        fields = ['book', 'member', 'borrow_date', 'Return_date']
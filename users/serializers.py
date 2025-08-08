from rest_framework import serializers
from users.models import Author, Member

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id','name', 'email', 'membership_date']
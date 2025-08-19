from rest_framework import serializers
from books import models as bookModels
from users import models as userModels


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModels.Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):

    author = BookAuthorSerializer(read_only=True)

    authorized_by = serializers.PrimaryKeyRelatedField(
        queryset =userModels.Author.objects.all(),
        source = 'author',
        write_only = True
    )

    class Meta:
        model = bookModels.Book
        fields = ['id', 'title','category', 'author','authorized_by' , 'availability_status', 'isbn']





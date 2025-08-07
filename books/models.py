from django.db import models
from users.models import Author

# Create your models here.

class Book(models.Model):
    status_choices = [
        ('AVAILABLE' , 'Available'),
        ('RESERVED' , 'Reserved'),
        ('BORROWED' , 'Borrowed')
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author , on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique= True)
    category = models.CharField(max_length=100)
    availability_status = models.CharField(max_length=15, choices=status_choices, default= 'AVAILABLE')

    def __str__(self):
        return self.title
    
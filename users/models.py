from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.CharField()

    def __str__(self):
        return f"Author of the book is {self.name}"
    

class Member(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    membership_date = models.DateField(auto_now= True)

    def __str__(self):
        return f"member : {self.name}"

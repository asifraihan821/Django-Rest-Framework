from django.db import models
from books.models import Book
from users.models import Member

# Create your models here.


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name= 'borrow_records')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateTimeField(auto_now_add=True)
    Return_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
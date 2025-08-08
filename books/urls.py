from django.urls import path
from books import views

urlpatterns = [
    path('<int:pk>/',views.books,name='book-view'),
    path('',views.all_books, name="all-books")
]

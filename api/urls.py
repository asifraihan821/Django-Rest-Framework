from django.urls import path,include



urlpatterns = [
    path('books/',include('books.urls')),
    path('authors/',include('users.author_urls')),
    path('members/',include('users.members_urls'))
]

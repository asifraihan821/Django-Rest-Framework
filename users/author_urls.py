from django.urls import path,include
from users import views

urlpatterns = [
    path('',views.view_authors,name='all-authors'),
    path('<int:pk>/',views.view_specific_author)
]
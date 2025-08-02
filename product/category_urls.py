from django.urls import path
from product import views



urlpatterns = [
    path('<int:pk>/',views.view_category, name='view-specific-category'),
    path('nothing/',views.view_nothing),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('students/', views.student_list, name='student_list'),
    path('', views.home, name='home'),
    path('books/add/', views.add_book, name='add_book'),
    path('students/add/', views.add_student, name='add_student'),
]

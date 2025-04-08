from django import forms
from .models import Book, Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

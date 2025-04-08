from django.shortcuts import render, redirect
from .models import Book, Student
from .forms import BookForm, StudentForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'library/student_list.html', {'students': students})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'library/add_student.html', {'form': form})


def home(request):
    return render(request, 'index.html')
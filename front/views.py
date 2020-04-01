from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    SQL = r'SELECT * FROM book;'
    cursor.execute(SQL)
    books = cursor.fetchall()
    return render(request, 'index.html', context={'books': books})


def add_book(request):
    return render(request, 'add_book.html')


def book_detail(request):
    return render(request, 'book_detail.html')

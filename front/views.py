from django.shortcuts import render,redirect,reverse
from django.db import connection


def index(request):
    cursor = connection.cursor()
    SQL = r'SELECT * FROM book;'
    cursor.execute(SQL)
    books = cursor.fetchall()
    return render(request, 'index.html', context={'books': books})


def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    else:
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        cursor = connection.cursor()
        SQL = r"INSERT INTO book(id ,name, author) values(null, '{a}','{b}')".format(a=book_name, b=book_author)
        cursor.execute(SQL)
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = connection.cursor()
    SQL = r"SELECT * FROM book WHERE id='{id}'".format(id=book_id)
    cursor.execute(SQL)
    book = cursor.fetchone()
    return render(request, 'book_detail.html', context={'book':book})


def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = connection.cursor()
        SQL = r"DELETE FROM book WHERE id='{id}'".format(id=book_id)
        cursor.execute(SQL)
        print(SQL)
        return redirect(reverse('index'))
    else:
        return RuntimeError('提交方法不是POST')

import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from . import models


def book_view(request):
    if request.method == 'GET':
        books = Book.objects.filter().order_by('-id')
        return render(request, template_name='book.html', context={'books': books})


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        return render(request, template_name='book_detail.html', context={'book_id': book_id})


def about_views(request):
    if request.method == 'GET':
        return HttpResponse('I am Kanbolot Abibillaev. I am 20 yrs')


def hobbies_views(request):
    if request.method == 'GET':
        return HttpResponse('My hobby is reading books and horse riding')


def current_time_views(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().strftime('%I:%M:%S %p'))


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.filter().order_by('-id')
        return render(request, template_name='books/book_list.html',
                      context={'books': books})


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(request, template_name='books/book_detail.html',
                      context={'book_id': book_id})

from re import T
from urllib import request
from django.shortcuts import render,redirect
from .models import Book, Category
from booksTransaction.models import Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
cats=Category.objects.all()


@login_required(login_url='login')
def home(request):
    books=Book.objects.all()
    return render(request,'list_books.html',{'books':books,'cats':cats,'title':'Home'})


@login_required(login_url='login')
def list_books(request,cat_id):
    books=Book.objects.all().filter(cat_id=cat_id)
    cat=Category.objects.get(pk=cat_id)
    if books:
        return render(request,'list_books.html',{'books':books,'cats':cats,'title':cat.name})
    else:
        messages.error(request, 'No books found!')
        return render(request,'list_books.html',{'cats':cats,'title':cat.name})


@login_required(login_url='login')
def search_books(request):
    if(request.method=="POST"):
        searched=request.POST['searched']
        books=Book.objects.filter(book_title__contains=searched)| Book.objects.filter(author_name__contains=searched)|Book.objects.filter(publication_year__contains=searched)
        if books:
            return render(request,'list_books.html',{'searched':searched,'books':books,'cats':cats,'title':searched})
        else:
            messages.error(request, 'No books found!')
            return render(request,'list_books.html',{'cats':cats,'title':searched})
    else:
        return render(request,'list_books.html',{'cats':cats})

@login_required(login_url='login')
def book_detail(request,book_id):
    book=Book.objects.get(pk=book_id)
    return render(request,'book_detail.html',{'book':book,'cats':cats,'title':book.book_title})

@login_required(login_url='login')
def books_author(request,author_name):
    book=Book.objects.filter(author_name=author_name)
    return render(request,'list_books.html',{'books':book,'cats':cats,'title':author_name})
    
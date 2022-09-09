from urllib import request
from django.shortcuts import render,redirect
from books.models import Book,Category
from django.contrib import messages
from .models import Borrowing, Reservation
from django.contrib.auth.models import User
from datetime import timedelta
import datetime
from django.contrib.auth.decorators import login_required
cats=Category.objects.all()
# Create your views here.
@login_required(login_url='login')
def borrow_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    borrow=Borrowing.objects.filter(book=book).filter(user=member)
    if borrow:
        messages.error(request, 'Book already borrowed')
        return redirect('home')
    else:
        book.number_of_copies-=1
        book.save()
        borrow=Borrowing.objects.create(book=book,user=member)
        messages.success(request, 'Book borrowed successfully')
        return render(request,"borrowed_successfully.html",{'cats':cats})
@login_required(login_url='login')
def borrowed_books(request,user_id):
    member=User.objects.get(pk=user_id)
    borrowed_books=Borrowing.objects.filter(user=member)
    return render(request,"borrowed.html",{'books':borrowed_books,'cats':cats})

@login_required(login_url='login')
def reserved_books(request,user_id):
    member=User.objects.get(pk=user_id)
    reserved_books=Reservation.objects.filter(user=member)
    return render(request,"reserved.html",{'books':reserved_books,'cats':cats})


@login_required(login_url='login')
def renew_borrowing(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    borrowed_books=Borrowing.objects.filter(user=member)
    borrowed_book=Borrowing.objects.get(user=member,book=book)
    borrowed_book.renew_borrowing=True
    borrowed_book.return_date+=timedelta(days=10)
    borrowed_book.save()
    return render(request,"borrowed.html",{'books':borrowed_books,'cats':cats})


@login_required(login_url='login')
def reserve_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(pk=user_id)
    reserve=Reservation.objects.filter(user=member,book=book)
    b_book=Borrowing.objects.filter(user=member,book=book)
    if reserve:
        messages.error(request, 'Book already reserved')
        return redirect('home')
    else:
        if b_book:
            messages.error(request, 'Book already borrowed')
            return redirect('home')
        else:
            reserve=Reservation.objects.create(book=book,user=member)
            messages.success(request, 'Book reserved successfully')
            return render(request,"reserved_successfully.html",{'cats':cats})

@login_required(login_url='login')
def cancel_reservation(request,book_id,user_id):
    user=User.objects.get(pk=user_id)
    book=Book.objects.get(pk=book_id)
    res=Reservation.objects.get(book=book,user=user)
    res.delete()
    all_res=Reservation.objects.filter(user=user)
    if all_res:
        return render(request,'reserved.html',{'books':all_res,'cats':cats})
    else:
        messages.warning(request,"No reserved books")
        return render(request,'reserved.html',{'cats':cats})
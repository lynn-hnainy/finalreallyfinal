from re import U
from unittest import result
from django.shortcuts import render,redirect
from booksTransaction.models import Borrowing, Reservation
from books.models import Book
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def welcome(request):
    return render(request,'Welcome.html',{'message':'hello'})

@login_required(login_url='login')
def search_user(request):
    if(request.method=="POST"):
        searched=request.POST['searched']
        if searched != "":
            user=User.objects.filter(username__contains=searched)
            if user:
                return render(request,'result.html',{'users':user})
            else:
                messages.error(request, 'User not found')
                return render(request,'welcome.html')
        else:
            messages.error(request, 'Please enter username')
            return render(request,'welcome.html')
    else:
        return render(request,'Welcome.html')

@login_required(login_url='login')
def user_books(request,user):
    user=User.objects.get(username=user)
    b_books=Borrowing.objects.filter(user=user)
    if b_books:
        return render(request,"user_books.html",{'borrowed':b_books})
    else:
        messages.error(request,'No borrowed books')
        return render(request,'user_books.html')

@login_required(login_url='login')
def return_book(request,book_id,user_id):
    #get the correct user and the correct book
    user=User.objects.get(id=user_id)
    book=Book.objects.get(id=book_id)

    #delete the borrowing transaction from the table
    borr=Borrowing.objects.filter(book=book,user=user)
    borr.delete()

    #select this book woth minimum reservation date to make it available again
    res_book=Reservation.objects.filter(book=book).order_by('reservation_date')[0]
    res_book.is_ready=True
    res_book.save()

    #select the remaining borrowed books
    b_books=Borrowing.objects.filter(user=user)

    #update the number of copies of the book
    book.number_of_copies+=1
    book.save()
    messages.success(request,"Book returned")
    return render(request,"user_books.html",{'borrowed':b_books})
from pyexpat import model
from zoneinfo import available_timezones
from django.db import models
from books.models import Book
from members.models import Member
from datetime import date, timedelta
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Borrowing(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    borrow_date=models.DateField(default=datetime.datetime.now())
    return_date=models.DateField(blank=True, null=True)
    renew_borrowing=models.BooleanField(default=False)
    def clean(self):
        if not self.return_date:
            self.return_date = self.borrow_date + timedelta(days=10)



    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)


    def __str__(self):
        return self.user.username+' '+self.book.book_title

    @property
    def fines(self):
        return ((datetime.date.today()-self.return_date).days)*5*1000

class Reservation(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reservation_date= models.DateField(default=datetime.datetime.now())
    is_ready=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    @property
    def availibility_date(self):
        book=Borrowing.objects.filter(book=self.book)
        if book:
            availibility_date=book.order_by('return_date')[0]
            return availibility_date.return_date

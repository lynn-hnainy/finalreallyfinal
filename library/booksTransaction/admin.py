from django.contrib import admin
from .models import Borrowing
from .models import Reservation
# Register your models here.
admin.site.register(Borrowing)
admin.site.register(Reservation)

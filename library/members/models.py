from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    phone = models.CharField(null=True,max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    birthdaydate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.user.username

from pyexpat import model
import this
from django.db import models
import books

# Create your models here.
class Language(models.Model):
    name=models.CharField('lang_name',max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField('cat_name',max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_title=models.CharField('book_title',max_length=120)
    description=models.TextField('description',null=True)
    author_name=models.CharField('author_name',max_length=120)
    number_of_pages=models.IntegerField('number_of_pages')
    number_of_copies=models.IntegerField('number_of_copies')
    publication_year=models.IntegerField('publication_year')
    lang_id=models.ForeignKey(Language,on_delete=models.CASCADE)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    book_img=models.ImageField(null=True,blank=True,upload_to="assets/")

    def __str__(self):
        return self.book_title+'-'+self.author_name

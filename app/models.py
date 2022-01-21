from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

class Book(models.Model):
    book_name=models.CharField(max_length=50,blank=True, default=None)
    book_author=models.CharField(max_length=50)
    book_edition=models.IntegerField()
    book_price=models.IntegerField()
    
    def __str__(self):
        return str(self.id)

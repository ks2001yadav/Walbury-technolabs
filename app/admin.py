from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','book_name', 'book_author', 'book_edition','book_price', )

admin.site.register(Book, BookAdmin)


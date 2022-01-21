from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import  CustomerRegistrationForm,BookForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Book
import random
import http.client
from django.conf import settings
from twilio.rest import Client



def home(request):
    return render(request,'home.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
           email=request.POST.get('email')
           name=request.POST.get('username')

           check_user=User.objects.filter(email=email).first()
           if check_user:
               messages.success(request,'User already exits')
               return render(request,'register.html',{'form':form})

           messages.success(request,'Congratulations, registered successfully')
           user = form.save( commit= False)
           user.save()
#        
        return render(request,'customerregistration.html',{'form':form})


class AddBookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,'addbook.html',{'form':form})
    def post(self,request):

        form=BookForm(request.POST)
        if form.is_valid():
            book_name = request.POST.get('book_name')
            book_author = request.POST.get('book_author')
            book_edition = request.POST.get('book_edition')
            book_price= request.POST.get('book_price')
            # print(book_name)
            Book(book_name =book_name ,book_author=book_author,book_edition=book_edition, book_price = book_price).save()
            
            messages.success(request,'Congratulations!! Book add successfully')
        return render(request,'addbook.html',{'form':form})


def listbook(request):

    data = Book.objects.all()
   
    stu = {
    "s": data
    }
   
    return render(request,"listbook.html",stu)

def edit(request,id):
    book = Book.objects.filter(id=id)[0] 
    Book.objects.filter(id=id).delete()
    data_dict = {'book_name':book.book_name,'book_author':book.book_author,'book_edition':book.book_edition,'book_price':book.book_price,}
    form=BookForm(data_dict)
    return render(request, 'edit.html', {'form':form,'book':book})  


def delete(request,id):
    Book.objects.filter(id=id).delete()
    data = Book.objects.all()
   
    stu = {
    "s": data
    }
    messages.success(request,'Congratulations!! Book deleted successfully')
    return render(request,'home.html') 


def update(request,id):

    if request.method == 'POST':
            book_name = request.POST.get('book_name')
            book_author = request.POST.get('book_author')
            book_edition = request.POST.get('book_edition')
            book_price= request.POST.get('book_price')
            messages.success(request,'Congratulations!! Book add successfully')
           
            book = Book(book_name =book_name ,book_author=book_author,book_edition=book_edition, book_price = book_price)
            book.save()
        
    return redirect('/listbook')  



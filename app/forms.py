
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext,gettext_lazy as _
from .models import Book

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = [
#         'book_name',
#         'book_author',
#         'book_edition',
#         'book_price'
#         ]

class BookForm(forms.Form):
    book_name = forms.CharField(label='Book Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    book_author=forms.CharField(label='Book Author',widget=forms.TextInput(attrs={'class':'form-control'}))
    book_edition=forms.IntegerField(label='Book edition', widget=forms.TextInput(attrs={'class':'form-control'}))
    book_price = forms.IntegerField(label='Book Price',widget=forms.TextInput(attrs={'class':'form-control',}))



class CustomerRegistrationForm(UserCreationForm) :
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True ,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email']
        labels={'email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class MyPasswwordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from models import Product
from django.forms import ModelForm
import re

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

#class Userform(ModelForm):
#    password=forms.CharField(widget=forms.PasswordInput())

#    class meta:
#        model=User
#        fields={'Firstname','Lastname','email','password'}

#    def __init__(self,*args,**kwargs):
#        super(Userform, self).__init__( *args, **kwargs)
#        self.fields['Firstname'].widget.attrs.update({'class':'form-control','placeholder':'Firstname'})
#        self.fields['Lastname'].widget.attrs.update({'class':'form-control','placeholder':'Lastname'})
#        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
#        self.fields['password'].widget.attrs.update({'class':'form-control','placeholder':'Password'})

#class ProductForm(ModelForm):
#        model = Product
#        fields=('productName','description','quantity','price','status')

#    def __init__(self,*args,**kwargs):
#        super(ProductForm, self).__init__( *args, **kwargs)
#        self.fields['productName'].widget.attrs.update({'class':'form-control','placeholder':'productName'})
#        self.fields['description'].widget.attrs.update({'class':'form-control','placeholder':'description'})
#        self.fields['quantity'].widget.attrs.update({'class':'form-control','placeholder':'quantity'})
#        self.fields['price'].widget.attrs.update({'class':'form-control','placeholder':'price'})
#        self.fields['status'].widget.attrs.update({'class':'form-control','placeholder':'status'})
#        self.fields['productName'].required = True

from django import forms
from wolfapp.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmpForm(forms.Form):
    name=forms.CharField(max_length=50)
    empid=forms.IntegerField()
    sal=forms.FloatField()

class ProductModelForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    price=forms.IntegerField()
    status=forms.BooleanField()

    class Meta:
        model=Product
        fields=['name','price','status']

class UserRegister(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

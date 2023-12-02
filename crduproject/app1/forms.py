from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Books
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser




class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        password1 = forms.CharField(widget=forms.PasswordInput)
        password2= forms.CharField(widget=forms.PasswordInput)
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')




class ItemForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name' , 'Author' , 'description', 'price')
        labels = {
            'name' : '',
            'Author' : '',
            'description' : '',
            'price' : '',
        }




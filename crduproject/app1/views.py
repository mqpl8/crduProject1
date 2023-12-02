from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import  MyUser,Books
from .forms import ItemForm,MyUserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


# Create your views here.


class uaddItemForm(forms.ModelForm):
    class Meta:
        model = Books   
        fields = "__all__"



def index(request):

    return render(request,'app1/menu.html')




def login_view (request) :

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # replace 'home'with the name of your home page URL pattern
            # url = reverse('BooksStore/register')
            return redirect(reverse("app1:Booksu"))
        else:
            # handle invalid login credentials
            return redirect(reverse("app1:login"))
            pass
    else:
        return render(request, 'app1/login.html')



def signup_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app1:login'))
    else:
        #alret
        form = MyUserCreationForm()

    return render(request, 'app1/signup.html', {'form': form})



def Booksu(request):
    return render(request,'app1/allItems.html',{
        'books':Books.objects.all()
    })
    
#here in add i must check.

def add(request, book_id):
    
    if request.method == 'POST':
        book = Books.objects.get(id=book_id)
        username = request.user.username
        user = MyUser.objects.get(username=username)
        if request.user.is_authenticated:
            user.cart.add(book)
        else:
            return render(request,'app1/detalisItem.html', {
                'Books': book
            })
    else:
        book = Books.objects.get(id=book_id)



    return render(request,'app1/detalisItem.html', {
        'Books': book
    })



def addform(request):
    if request.method == 'POST':

        form = uaddItemForm(request.POST)
        if (form.is_valid()):
            form.save()

    else:
        form = uaddItemForm()

    return render(request,"app1/addItem.html",
        {"form": uaddItemForm()})



def update(request,book_id):
    Book = Books.objects.get(id = book_id)
    form = ItemForm(request.POST or None,instance=Book)
    if form.is_valid():
        form.save()

    return render(request, "app1/updateItem.html",
        {'book':Book,
        'form':form})
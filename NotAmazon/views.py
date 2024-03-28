from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ("username", "email", "password1", "password2")

# Create your views here.
def index(request):
    context = {}
    context["Title"] = "HOME"
    return render(request, "home.html", context)

def products(request):
    return render(request, "products.html", {})

def shop(request):
    item_list = Item.objects.all()
    context = {"item_list":item_list}
    return render(request, "shop.html", context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password1=password)
        if user is not None:
            form = login(request, user)
            return redirect("home.html")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form":form})

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    
    return render(request, "registration/signup.html", {"form":form})

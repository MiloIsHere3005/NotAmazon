from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import Login_Form
from .models import Item

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

def user_login(request):
    if request.method == "POST":
        form = Login_Form(request.POST)
        form.user_email = request.POST["user_email"]
        form.user_pass = request.POST["user_pass"]
        user = authenticate(request, user_email=form.user_email, user_pass=form.user_pass)
        if user is not None:
            login(request, user)
            return redirect("home.html")
        else:
            return redirect("user_login.html")
    else:
        return render(request, "user_login.html", {"form":Login_Form})

def user_signup(request):
    return render(request, "user_signup.html", {})

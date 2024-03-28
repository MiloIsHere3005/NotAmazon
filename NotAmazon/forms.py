from django.forms import ModelForm
from django import forms
from .models import User

class Login_Form(ModelForm):
    user_email = forms.TextInput()
    user_pass = forms.TextInput()

    class Meta:
        model = User
        fields = ["user_email", "user_pass"]
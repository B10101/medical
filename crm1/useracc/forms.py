from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class Orderform(ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer','Id_number', 'doctor', 'date_reserved']

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Customer, Vaccine, Reservation
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CustomerForm, Orderform
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('contact-name')
        email = request.POST.get('contact-email')
        message = request.POST.get('contact-project')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'useracc/index.htm')


def register(request):
    if request.user.is_authenticated:
        return redirect('user')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')

                messages.success(request, 'Account created for ' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'useracc/register.htm', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('user')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('user')

            else:
                messages.error(request, 'Username or password is incorrect')

    return render(request, 'useracc/login.htm')


@login_required(login_url='login')
def user(request):
    return render(request, 'useracc/user.htm')


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def create_order(request):
    form = Orderform()
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
    context = {"form":form}
    return render(request, 'useracc/reserve.htm', context)

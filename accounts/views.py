from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages

# Create your views here.
def registerPage(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            username = email.split('@')[0]
            password = form.cleaned_data['password']

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()      
            messages.success(request,'Registration Successful')
            return redirect('register')

    context = {'form':form}
    return render(request,'accounts/register.html',context)


def loginPage(request):
    context = {}
    return render(request,'accounts/login.html',context)


def logoutPage(request):
    context = {}
    return 
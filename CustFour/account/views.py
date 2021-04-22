from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.http import HttpResponse
User = get_user_model()

# Create your views here.

def home(request):
    return render(request, 'html/home.html')



def register(request):
    if(request.method=='POST'):
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phone = request.POST['mobile_number']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1==password2):
            if(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email has been Taken')
                return redirect('/register')
            else:
                user=User.objects.create_user(firstname=firstname, lastname=lastname, phone=phone,
                                              email=email, password=password1)
                user.save()
                print("user created")
                return redirect('/login')

        else:
            messages.info(request, 'Password not matched')
            return redirect('/register')

    else:
        return render(request, 'html/register.html')


def login(request):
    if(request.method=='POST'):
        email = request.POST['email']
        print("**********************")
        print(email)
        password = request.POST['password']
        print(password)

        user = auth.authenticate(email=email, password=password)
        print(user)
        if (user is not None):
            auth.login(request, user)
            request.session.set_expiry(300) # in second for automatic logout
            return redirect('/welcome')
        else:
            messages.info(request, 'Invalid Credentails')
            return redirect('/login')
    else:
        return render(request, 'html/login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/')


def welcome(request):
    return HttpResponse("your are sucessfully logged In")
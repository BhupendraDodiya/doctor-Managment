from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Doctor
# Create your views here.


def index(request):
    return render(request, "signup.html")


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        degree = request.POST['degree']
        contact = request.POST['contact']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        image = request.FILES.get('image')
        category = request.POST['category']
        if Doctor.objects.filter(Email=email).exists():
            messages.error(request, "Email already exist")
            return redirect('/')
        elif Doctor.objects.filter(Contact=contact).exists():
            messages.error(request, "Contact already exist")
            return redirect('/')
        else:
            Doctor.objects.create(Name=name, Degree=degree, Contact=contact,
                                  Email=email, Password=password, Image=image, Category=category)
            return redirect('/login/')


def login(request):
    return render(request, 'login.html')


def lreg(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Doctor.objects.filter(Email=email).exists():
            res = Doctor.objects.get(Email=email)
            psw = res.Password
            if check_password(password, psw):
                return redirect('/table/')
            else:
                messages.error(request,'password not valid')
                return redirect('/login/')
        else:
            messages.error(request,'Email not valid')
            return redirect('/login/')


def table(request):
    res = Doctor.objects.all()
    return render(request, 'table.html', {'res': res})


def delete(request, uid):
    Doctor.objects.filter(id=uid).delete()
    return redirect('/table/')

def update(request,uid):
    res = Doctor.objects.get(id=uid)
    return render(request,'update.html',{'res':res})

def ureg(request):
    if request.method =="POST":
        hide = request.POST['hide']
        name = request.POST['name']
        degree = request.POST['degree']
        contact = request.POST['contact']
        email = request.POST['email']
        category = request.POST['category']
        Doctor.objects.filter(id=hide).update(Name=name,Degree=degree,Contact=contact,
                                              Email=email,Category=category)
        return redirect('/table/')
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('password')
        address=request.POST.get('address')
        User.objects.create_user(username=username, password=password, phone=phone, address=address)
        return redirect('user:login')
    else:
        return HttpResponse("허용되지 않은 접근 방식입니다.")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('user:home')
        else:
            return HttpResponse('로그인 실패')

def home(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return redirect('/login/')
        return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def student_login(request):
    if request.method == 'post':
        user = auth.authenticate(rollnumber=request.POST['rollnumber'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home.html')
        else:
            return render(request,'student_login.html',{'error':'Roll Number or Password incorrect.'})
    else:
        return render(request,'student_login.html')

def student_register(request):
    return render(request,'student_register.html')
    """if request.method == 'post':
        # user has info and wants to create an account now.
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.get(rollnumber=request.POST['rollnumber'])
            return render(request, 'student_register.html', {'error':'Roll Number already exixts.'})
    else:
        return render(request,'student_register.html')"""
   
        
    
def student_viewing(request):
    return render(request,'student_viewing.html')


from django.shortcuts import render

# Create your views here.
def student_login(request):
    return render(request,'student_login.html')
def student_register(request):
    return render(request,'student_register.html')
def student_viewing(request):
    return render(request,'student_viewing.html')


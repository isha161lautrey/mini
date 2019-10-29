
from django.contrib import admin
from django.urls import path, include
from . import views
app='student'
urlpatterns = [
    
    path('student_login',view=views.student_login,name='student_login'),
    path('student_register',view=views.student_register,name='student_register'),
    path('student_viewing',view=views.student_viewing,name='student_viewing'),
]

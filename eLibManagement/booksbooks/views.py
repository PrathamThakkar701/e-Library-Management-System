from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import logout

def home(request):
    return render(request, "index.html", context={})

def save_student(request):
    student_name=request.POST['student_name']
    return render(request, "welcome.html", context = {'student_name':student_name})

def logout_view(request):
    logout(request)
    return redirect("/")
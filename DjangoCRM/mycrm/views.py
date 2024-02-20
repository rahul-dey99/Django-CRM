from django.shortcuts import render, render

def home(request):
    return render(request, 'home.html', {})

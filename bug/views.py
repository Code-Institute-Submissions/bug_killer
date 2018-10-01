from django.shortcuts import render, get_object_or_404, redirect

def get_home(request):
    return render(request, "home.html")

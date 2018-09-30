from django.shortcuts import render, get_object_or_404, redirect

def get_intro(request):
    return render(request, "intro.html")

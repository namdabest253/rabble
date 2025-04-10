from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {"welcome": str(request.user)}

    return render(request, "rabble/index.html", context)

def profile(request):
    context = {"username" : str(request.user), "email": str(request.user.email)}
    
    return render(request, "rabble/profile.html", context)

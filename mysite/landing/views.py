from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the webapp index.")
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login-page.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == "POST":
        # Need to add new user to database
        print()
        print("Congradulations " + request.POST['email'] + " signed up!!")
        print("Do something fun here.")
        print()
    return render(request, 'main.html') # Need to find a way to redirect the user vs rendering
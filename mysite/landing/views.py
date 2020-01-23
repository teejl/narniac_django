from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world. You're at the webapp index.")
    return render(request, 'index.html')

def login_page(request):
    #return render(request, 'login-page.html') # login not enabled yet
    return render(request, 'main.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == "POST":
        # Need to add new user to database
        update_user(request.POST['email'])
        print("the user has been added to the list.")
        print()
    # Redirect to home page
    return render(request, 'main.html') # Need to find a way to redirect the user vs rendering

def update_user(email):
    import os
    import pandas as pd
    # Talk to the console
    print("\n", " ~~~ Adding a user to the database of users... ~~~~ ", "\n", "Adding the following user: ",  email, "\n")

    # print current working directory
    usrpath = os.path.join(os.getcwd(), "data", "Users.txt")

    # open the list of users and add the new user
    usrs = pd.read_csv(usrpath)
    if email not in list(usrs['Email']):
        usrs = usrs.append({"Email": email}, ignore_index=True)
        usrs.to_csv(usrpath, index=False)
        print("Adding user to the list...")
    else:
        print("User is already on the list!", "\n")

    # talk to the server
    print(" ~~~ Updated userlist ~~~ ", "\n", usrs, "\n")

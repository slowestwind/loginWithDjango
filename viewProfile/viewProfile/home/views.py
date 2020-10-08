
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate


def index(request):
    #checking if the user is anonymous
    print(request.user.is_anonymous)
    if request.user.is_anonymous:
        return redirect('/loginUser')
    return render(request, 'index.html')

def loginUser(request):
    # if the request method is post
    # testuser3 Admin@123
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/loginUser")




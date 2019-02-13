import json
from django.utils.safestring import mark_safe
from django.shortcuts import render

from .models import registerUser


def index(request):
    return render(request, 'Chat_App/index.html', {})


def room(request, room_name):
    return render(request, 'Chat_App/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def base(request):
    return render(request, 'Chat_App/base.html')


def signupView(request):
    return render(request, 'Chat_App/register.html', {})


def addUser(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['psw']

    all_users_db = registerUser.objects.all()
    for user in all_users_db:
        if user.emailid != email:
            all_users = registerUser(firstname=fname, lastname=lname, emailid=email, password=password)
            all_users.save()
            return render(request, 'Chat_App/login.html', {'all_users': all_users_db})
        else:
            return render(request, 'Chat_App/register.html', {'error': "user already registered"})


def loginView(request):
    return render(request, 'Chat_App/login.html', {})


def chatView(request):
    all_users = registerUser.objects.all()
    email = request.POST['uname']
    password = request.POST['psw']

    for user in all_users:
        if user.emailid == email and user.password == password:
            name = user.firstname
            return render(request, 'Chat_App/index.html', {'name': name})

    return render(request, 'Chat_App/login.html', {'error': "**invalid username and password"})

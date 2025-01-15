from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db import models
from django.contrib.auth import authenticate, login as authlogin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            authlogin(request, user)
            return redirect('/home')
        else:
            print('waHAHAAHHA')
            error_message = 'Invalid username or password'
    template = loader.get_template('form.html')
    return render(request, 'form.html', {'error_message': error_message})


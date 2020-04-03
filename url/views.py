from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import Url, CreateUser
from .models import UrlData

import random
import string


@login_required(login_url='url:login')
def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            request.user.urlshort.add(new_url)
            return redirect('/')
    else:
        form = Url()
    data = UrlData.objects.filter(user=request.user)
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


@login_required(login_url='url:login')
def urlS(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username OR password is Invalid")
    context = {}
    return render(request, 'login.html', context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                messages.success(
                    request, f"Account Was Created Successfully for {username}")
                return redirect('/login')
    form = CreateUser()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')

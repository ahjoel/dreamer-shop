from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import unauthenticated_user
from accounts.models import User


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # auth.login(request, user)
            login(request, user)
            # messages.success(request, 'You are now logged in.')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists !')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists !')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    auth.login(request, user)
                    # messages.success(request, 'You are now logged in.')

                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('accounts:dashboard')
                    user.save()
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='accounts:login')
def dashboard(request):
    data = {

    }
    return render(request, 'accounts/dashboard.html', data)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from core.models.auth import User


def sign_in(request):
    ctx = {}
    if request.POST:
        password = request.POST.get('password')
        username = request.POST.get('username')

        if password is None or username is None:
            ctx['login_error'] = 'Username and Password required'
            return render(request, "auth/login.html", ctx)
        user = User.objects.filter().first()
        if not user:
            ctx['login_error'] = 'User Not Found'
            return render(request, "auth/login.html", ctx)
        if not user.check_password(password):
            ctx['login_error'] = 'Password is invalid'
            return render(request, "auth/login.html", ctx)

        login(request, user)
        return redirect("home")

    return render(request, "auth/login.html", ctx)









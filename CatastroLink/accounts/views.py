from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()

            # Log the user in after registration
            login(request, user)
            return redirect(
                "home"
            )  # Redirect to the home page or wherever you want
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to the home page
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

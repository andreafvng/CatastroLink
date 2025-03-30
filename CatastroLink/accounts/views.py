from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import SimpleUserRegistrationForm


def register(request):
    if request.method == "POST":
        form = SimpleUserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data["password"]
            )  # Hash the password
            user.save()

            # Log the user in
            user = authenticate(
                username=user.username, password=form.cleaned_data["password"]
            )
            login(request, user)

            return redirect(
                "home"
            )  # Redirect to a home page or somewhere else after successful registration
    else:
        form = SimpleUserRegistrationForm()

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

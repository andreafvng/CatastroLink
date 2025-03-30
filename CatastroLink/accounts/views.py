from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from utils.geo import get_lat_lon_from_text
from .forms import UserTypeSelectionForm
from .models import AppUser

from .forms import SimpleUserRegistrationForm


def register(request):
    if request.method == "POST":
        form = SimpleUserRegistrationForm(request.POST)

        if form.is_valid():
            home_address = form.cleaned_data["home_address"]
            latitude, longitude = get_lat_lon_from_text(home_address)

            # Save the user
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data["password"]
            )  # Hash the password

            user.latitude = latitude
            user.longitude = longitude

            user.save()

            # Log the user in
            user = authenticate(
                username=user.username, password=form.cleaned_data["password"]
            )
            login(request, user)

            # Redirect to a home page or somewhere else after successful registration
            return redirect("home")

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


def select_user_type(request, user_id):
    user = AppUser.objects.get(id=user_id)

    if request.method == "POST":
        form = UserTypeSelectionForm(request.POST)
        if form.is_valid():
            # Save the user's choice in the user_type field
            user.user_type = form.cleaned_data['user_type']
            user.save()
            return redirect('home')  # Redirect to home or another appropriate page
    else:
        form = UserTypeSelectionForm()

    return render(request, "select_user_type.html", {"form": form, "user": user})

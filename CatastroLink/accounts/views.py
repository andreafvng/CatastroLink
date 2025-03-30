import os

import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import SimpleUserRegistrationForm
from CatastroLink.filter import get_users_near_disaster


def get_lat_lon_from_text(address):
    api_key = os.getenv("GEOCODE_API_KEY")
    api_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

    response = requests.get(api_url)

    data = response.json()

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    return float(lat), float(lon)


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

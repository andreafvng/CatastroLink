import os
from geopy.distance import geodesic
from accounts.models import AppUser

import requests


def get_lat_lon_from_text(address):
    api_key = os.getenv("GEOCODE_API_KEY")
    api_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

    response = requests.get(api_url)

    data = response.json()

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    return float(lat), float(lon)


def filter_by_distance(reports, max_distance_km, n):
    clusters = []

    for report in reports:
        close_reports = [
            r
            for r in reports
            if geodesic((report.lat, report.lon), (r.lat, r.lon)).km
            <= max_distance_km
        ]

        if len(close_reports) >= n:
            clusters.append(close_reports)

    return clusters


def filter_users_by_distance(lat, lon, max_distance_km):
    # List to hold users within the distance range
    close_users = []

    # Loop through all users and check if they're within the given distance
    for user in AppUser.objects.all():
        user_location = (user.latitude, user.longitude)
        input_location = (lat, lon)

        # Calculate distance between the input location and the user's location
        distance = geodesic(input_location, user_location).km

        # If within the maximum distance, add to the result list
        if distance <= max_distance_km:
            close_users.append(user)

    return close_users

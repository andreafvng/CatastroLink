import os

import requests


def get_lat_lon_from_text(address):
    api_key = os.getenv("GEOCODE_API_KEY")
    api_url = f"https://geocode.maps.co/search?q={address}&api_key={api_key}"

    response = requests.get(api_url)

    data = response.json()

    lat = data[0].get("lat")
    lon = data[0].get("lon")

    return float(lat), float(lon)

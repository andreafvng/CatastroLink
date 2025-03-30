from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .filter import get_users_near_disaster 

def home(request):
    return render(request, "home.html")  # Render the home page template

def disaster_alert_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            lat = float(data.get("latitude"))
            lon = float(data.get("longitude"))

            if lat is None or lon is None:
                return JsonResponse({"error": "Latitude and longitude are required."}, status=400)

            clients, hosts = get_users_near_disaster((lat, lon))

            return JsonResponse({
                "clients": [user.username for user in clients],
                "hosts": [user.username for user in hosts],
            })

        except (ValueError, TypeError, KeyError):
            return JsonResponse({"error": "Invalid request data."}, status=400)

    return JsonResponse({"error": "POST request required."}, status=405)
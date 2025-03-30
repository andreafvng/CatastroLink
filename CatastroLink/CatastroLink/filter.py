from geopy.distance import geodesic

def get_users_near_disaster(disaster_location):
    clients = []
    hosts = []

    all_users = AppUser.objects.exclude(latitude=None).exclude(longitude=None)

    for user in all_users:
        user_location = (float(user.latitude), float(user.longitude))
        distance_km = geodesic(disaster_location, user_location).km  # Calculate distance

        if distance_km <= 5:
            if user.response == "client":
                clients.append(user)
            elif user.response == "host":
                hosts.append(user)
        elif 5 < distance_km <= 10 and user.response == "host":
            hosts.append(user)

    return clients, hosts

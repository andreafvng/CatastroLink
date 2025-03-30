from django.shortcuts import redirect, render
from django.utils.timezone import now, timedelta
from utils.geo import (
    filter_by_distance,
    filter_users_by_distance,
    get_lat_lon_from_text,
)

from .forms import DisasterReportForm
from .models import DisasterReport
from disaster_mode.models import Accommodation


def report_disaster(request):
    if request.method == "POST":
        form = DisasterReportForm(request.POST)

        if form.is_valid():
            address = form.cleaned_data["address"]
            lat, lon = get_lat_lon_from_text(address)

            if lat is None or lon is None:
                form.add_error(
                    "address",
                    "Could not determine location. Try a different address.",
                )
            else:
                DisasterReport.objects.create(
                    lat=lat,
                    lon=lon,
                    severity=form.cleaned_data["severity"],
                    description=form.cleaned_data["description"],
                )

                trigger_disaster_response()

                return redirect("home")  # Redirect to home or success page

    else:
        form = DisasterReportForm()

    return render(request, "reports/disaster_report.html", {"form": form})


def trigger_disaster_response():
    time_threshold = now() - timedelta(hours=1)  # last 1 hour
    recent_reports = DisasterReport.objects.filter(
        timestamp__gte=time_threshold
    )

    max_distance_km = 5  # maximum distance to cluster reports
    n = 3  # minimum number of reports to trigger a response

    disaster_clusters = filter_by_distance(recent_reports, max_distance_km, n)

    if disaster_clusters:
        print(
            f"Disaster response triggered with {len(disaster_clusters)} clusters."
        )

        # For each disaster cluster, calculate the average latitude and longitude
        for cluster in disaster_clusters:
            avg_lat = sum([report.lat for report in cluster]) / len(cluster)
            avg_lon = sum([report.lon for report in cluster]) / len(cluster)

            # Get users within 0-5 km (host or client) and 5-10 km (hosts only)
            hosts_or_client = filter_users_by_distance(avg_lat, avg_lon, 0, 5)
            hosts_only = filter_users_by_distance(avg_lat, avg_lon, 5, 10)

            # For users within 0-5 km, create both host and client records
            for user in hosts_or_client:
                host_or_client(user, host=True)  # Create host entry
                host_or_client(user, host=False)  # Create client entry

            # For users within 5-10 km, create only host records
            for user in hosts_only:
                host_or_client(user, host=True)  # Create host entry

    else:
        print("No disaster response needed.")


def host_or_client(user, host):
    # Create or update accommodation entry for the user as host or client
    accommodation, created = Accommodation.objects.get_or_create(
        user=user, host=host, matched=False
    )

    if not created:
        # If the accommodation already exists, you may want to update some fields
        accommodation.host = host
        accommodation.save()

    # Return the accommodation for further processing (if needed)
    return accommodation

from django.shortcuts import redirect, render
from django.utils.timezone import now, timedelta
from utils.geo import filter_by_distance, get_lat_lon_from_text

from .forms import DisasterReportForm
from .models import DisasterReport


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

    # to Andrea:
    # if disaster_clusters is not an empty list, then there is a cluster in which
    # to trigger a disaster response

    # this means a list of lists of reports, since disasters can happen all
    # around the world at the same time

    if disaster_clusters:
        print(
            f"Disaster response triggered with {len(disaster_clusters)} clusters."
        )
        # Logic to trigger disaster response goes here
    else:
        print("No disaster response needed.")

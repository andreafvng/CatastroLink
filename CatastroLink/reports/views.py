from django.shortcuts import redirect, render

from .forms import DisasterReportForm
from .models import DisasterReport

from utils.geo import get_lat_lon_from_text


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
                return redirect("home")  # Redirect to home or success page

    else:
        form = DisasterReportForm()

    return render(request, "reports/disaster_report.html", {"form": form})

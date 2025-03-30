from django.shortcuts import redirect, render

from .forms import AccommodationForm


def disaster_mode(request):
    return render(request, "disaster_mode/disaster_mode.html")


def seek_refuge(request):
    if request.method == "POST":
        form = AccommodationForm(request.POST)

        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.user = request.user
            accommodation.save()

            return redirect("disaster_mode:seek_refuge_matching")

    form = AccommodationForm()

    return render(request, "disaster_mode/seek_refuge.html", {"form": form})


def become_host(request):
    if request.method == "POST":
        form = AccommodationForm(request.POST)

        if form.is_valid():
            accommodation = form.save(commit=False)
            accommodation.user = request.user
            accommodation.host = True
            accommodation.save()

            return redirect("disaster_mode:become_host_matching")

    form = AccommodationForm()

    return render(request, "disaster_mode/become_host.html", {"form": form})


def seek_refuge_matching(request):
    return render(request, "disaster_mode/seek_refuge_matching.html")


def become_host_matching(request):
    return render(request, "disaster_mode/become_host_matching.html")

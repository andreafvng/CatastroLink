from django.shortcuts import render


def disaster_mode(request):
    return render(request, "disaster_mode/disaster_mode.html")


def seek_refuge(request):
    return render(request, "disaster_mode/seek_refuge.html")


def become_host(request):
    return render(request, "disaster_mode/become_host.html")

from django.urls import path
from . import views

app_name = "disaster_mode"

urlpatterns = [
    path("", views.disaster_mode, name="disaster_mode"),
    path("become-host/", views.become_host, name="become_host"),
    path("seek-refuge/", views.seek_refuge, name="seek_refuge"),
    path(
        "become-host/matching/",
        views.become_host_matching,
        name="become_host_matching",
    ),
    path(
        "seek-refuge/matching/",
        views.seek_refuge_matching,
        name="seek_refuge_matching",
    ),
]

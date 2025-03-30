from django.urls import path
from . import views

app_name = "disaster_mode"

urlpatterns = [
    path("", views.disaster_mode, name="disaster_mode"),
    path("become-host/", views.become_host, name="become_host"),
    path("seek-refuge/", views.seek_refuge, name="seek_refuge"),
]

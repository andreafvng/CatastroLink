from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", home, name="home"),
    path("reports/", include("reports.urls")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("preparation/", include("preparation.urls")),
    path("disaster_mode/", include("disaster_mode.urls")),
]

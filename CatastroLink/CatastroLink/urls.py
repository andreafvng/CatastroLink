from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import home, disaster_alert_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", home, name="home"),
    path("disaster_alert/", disaster_alert_view, name="disaster_alert"),
    path("reports/", include("reports.urls")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("preparation/", include("preparation.urls"))
]

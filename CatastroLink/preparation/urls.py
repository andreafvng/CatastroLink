from django.urls import path
from . import views

# Define the app namespace
app_name = "preparation"

urlpatterns = [
    path("", views.preparation, name="preparation")
]

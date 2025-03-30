from django.urls import path
from . import views

# Define the app namespace
app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="register"),  # Register page
    path("login/", views.login_view, name="login"),  # Login page
    # Other URL patterns for the 'accounts' app
]

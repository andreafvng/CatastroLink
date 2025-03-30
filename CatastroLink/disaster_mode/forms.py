from django import forms

from accounts.models import AppUser
from .models import Accommodation


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ["people", "pets", "accessibility"]


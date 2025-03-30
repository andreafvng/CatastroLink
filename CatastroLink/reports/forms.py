from django import forms
from .models import DisasterReport


class DisasterReportForm(forms.ModelForm):
    address = forms.CharField(max_length=255, required=True, label="Address")

    class Meta:
        model = DisasterReport
        fields = [
            "address",
            "severity",
            "description",
        ]  # No lat/lon since we compute them

from django import forms

from .models import AppUser


class SimpleUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput, label="Password confirmation"
    )
    home_address = forms.CharField(
        max_length=255, required=True, label="Home Address"
    )

    class Meta:
        model = AppUser
        fields = ["username", "home_address"]

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirmation

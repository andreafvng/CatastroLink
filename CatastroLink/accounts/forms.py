from django import forms
from django.contrib.auth.models import User


class SimpleUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput, label="Password confirmation"
    )

    class Meta:
        model = User
        fields = ["username"]  # Only include the username field

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirmation

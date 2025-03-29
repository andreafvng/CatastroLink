from django.db import models
from django.contrib.auth.models import geomodels

class User(AbstractUser):
    ROLE_CHOICES = [('client', 'Client'), ('host', 'Host')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    family_size = models.IntegerField(default=1)
    pets = models.BooleanField(default=False)
    accessibility_needs = models.TextField(blank=True)
    latitude = models.FloatField()  
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.username} - {self.role}"

class DisasterReport(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Report by {self.client.username} - {self.severity}"


class HostAvailability(models.Model):
    host = models.OneToOneField(User, on_delete=models.CASCADE, related_name='availability')
    max_clients = models.IntegerField()
    is_available = models.BooleanField(default=True)
    restrictions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.host.username} - Available: {self.is_available}"

class Match(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_clients')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match: {self.client.username} -> {self.host.username} ({self.status})"

class DisasterSummary(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    summary_text = models.TextField()

    def __str__(self):
        return f"Summary generated on {self.generated_at}"



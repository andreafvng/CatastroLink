from django.db import models

# Create your models here.
class DisasterReport(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.reported_at}"

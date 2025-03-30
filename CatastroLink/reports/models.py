from django.db import models


class DisasterReport(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    description = models.TextField()

    def __str__(self):
        return f"Report {self.id} - Severity {self.severity}"

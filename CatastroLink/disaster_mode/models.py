from django.contrib.auth import get_user_model
from django.db import models


from django.contrib.auth import get_user_model
from django.db import models


class Accommodation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    host = models.BooleanField(
        default=False
    )  # If True, user is a host; otherwise, a client
    people = models.TextField(max_length=500, null=True, blank=True)
    pets = models.TextField(max_length=500, null=True, blank=True)
    accessibility = models.TextField(max_length=500, null=True, blank=True)
    matched = models.BooleanField(default=False)

    # This field will store the matched accommodation (host-client pair)
    match = models.ForeignKey(
        "self",  # References another Accommodation instance
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # If the match is deleted, this field becomes null
        related_name="matches",
    )

    def __str__(self):
        return f"{'Host' if self.host else 'Client'} - {self.user.username}"

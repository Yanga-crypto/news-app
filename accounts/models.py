from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_types = [
        ("reader", 'Reader'),
        ("editor", 'Editor'),
        ("journalist", 'Journalist'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # choices are missing from the model
    role = models.TextField(choices=user_types, default="reader")

    # READER specific

    subscribed_journalists = models.ManyToManyField(User, blank=True, default=None, related_name="subscribed_users")
    subscribed_publishers = models.ManyToManyField("news.Publisher", blank=True, default=None, related_name="subscribed_users")

    # JOURALIST and EDITOR specific
    publisher = models.ForeignKey("news.Publisher", on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username

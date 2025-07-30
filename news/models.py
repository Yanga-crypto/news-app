from django.db import models
from django.contrib.auth.models import User


# Publisher model
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    # create a FK -> user to allow admin users to create publishers

    def __str__(self):
        return self.name


# Newsletter model
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    # A field with a ForeignKey
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


# Articles model
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    journalist = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True )
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

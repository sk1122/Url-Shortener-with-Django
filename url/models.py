from django.db import models
from django.contrib.auth.models import User


class UrlData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="urlshort", null=True)
    url = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return f"Short Url for: {self.url} is {self.slug}"

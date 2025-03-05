from django.db import models
from django.contrib.auth.models import User


class Checklist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ChecklistItem(models.Model):
    checklist = models.ForeignKey(
        Checklist, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

from django.db import models

from django.db import models

# Create your models here.
class Info(models.Model):
    slack_name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

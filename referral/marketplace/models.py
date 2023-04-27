from django.db import models

# Create your models here.
class Marketplace(models.Model):
    user = models.CharField(max_length=24)
    request = models.CharField(max_length=12)

from django.db import models

# Create your models here.
from django.db import models
from datetime import timedelta


class OldData(models.Model):
    image = models.URLField()


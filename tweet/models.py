from django.db import models


# Create your models here.

class tweep(models.Model):
    tweep = models.TextField(default="default")
    date_created = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.

class User_new(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
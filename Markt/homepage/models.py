from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    share_email = models.BooleanField(default=True)
    share_phone = models.BooleanField(default=False)

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    share_email = models.BooleanField(default=True)
    share_phone = models.BooleanField(default=False)

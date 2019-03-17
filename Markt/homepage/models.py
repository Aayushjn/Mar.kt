from django.db import models


class User(models.Model):
    id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=16)
    is_buyer = models.BinaryField()
    phone_number = models.CharField(max_length=10)
    share_email = models.BooleanField(default=True)
    share_phone = models.BooleanField(default=False)

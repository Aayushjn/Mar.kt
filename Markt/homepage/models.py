from django.db import models


class User(models.Model):
    id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=16)
    is_buyer = models.BinaryField()
    phone_number = models.CharField(max_length=10)
    share_email = models.BinaryField(default=True)
    share_phone = models.BinaryField(default=False)

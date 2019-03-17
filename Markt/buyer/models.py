from django.db import models

from Markt.homepage.models import User


class Product(models.Model):
    id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    vendor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BinaryField()
    description = models.CharField(max_length=300)
    minimum_bid = models.FloatField()
    current_high_bid = models.FloatField()
    image_link = models.CharField(max_length=100)

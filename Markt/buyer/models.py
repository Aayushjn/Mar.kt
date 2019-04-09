from django.db import models

from homepage.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    cat_id = models.IntegerField()
    vendor_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_id')
    is_sold = models.BooleanField(default=False)
    description = models.CharField(max_length=300)
    minimum_bid = models.FloatField()
    current_high_bid = models.FloatField()
    image_link = models.FileField(upload_to='./homepage/static/homepage/products')

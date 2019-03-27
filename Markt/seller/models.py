from django.db import models

from homepage.models import User


class Bid(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    product_id = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)


class Mail(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    message_type = models.PositiveSmallIntegerField()

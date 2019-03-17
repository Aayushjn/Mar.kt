from django.db import models

from Markt.homepage.models import User


class Bid(models.Model):
    id = models.IntegerField(max_length=10)
    product_id = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField()
    timestamp = models.DateTimeField()


class Mail(models.Model):
    id = models.IntegerField(max_length=10)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    message_type = models.IntegerField(max_length=5)

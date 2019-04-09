from django.db import models

from homepage.models import User

from buyer.models import Product


class Bid(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='p_id')
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='b_id')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)


class Mail(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buy_id')
    recv_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vend_id')
    bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)
    message_type = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)


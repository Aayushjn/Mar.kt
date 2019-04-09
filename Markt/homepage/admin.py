from django.contrib import admin

from homepage.models import User
from seller.models import Bid, Mail
from buyer.models import Product

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Mail)
admin.site.register(Product)

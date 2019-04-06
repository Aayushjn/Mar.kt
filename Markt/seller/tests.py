from django.test import TestCase, Client

from seller.models import Bid, Mail


# def create_bid(price:float, timestamp):
#     return Bid.objects.create(product_id=, buyer_id=, price=price, timestamp=timestamp)
#
# def create_mail(msg: int):
#     return Mail.objects.create(buyer_id=, vendor_id=, bid_id=, message_type=msg)

class TestSellerNavigation(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_dashboard_loadsCorrectTemplate(self):
        dashboard = self.client.get('seller/dashboard')
        self.assertTrue(dashboard.status_code, 200)

    def test_listing_loadsCorrectTemplate(self):
        listings = self.client.get('seller/dashboard/listings/')
        self.assertTrue(listings.status_code, 200)

    def test_item_loadsCorrectTemplate(self):
        item = self.client.get('seller/dashboard/item/')
        self.assertTrue(item.status_code, 200)

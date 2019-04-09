from django.test import TestCase, Client

from buyer.models import Product


# def create_product(name: str, category: int, is_sold: bool, min_bid: float, high_bid: float):
#     return Product.objects.create(name=name, category=category, vendor_id=, is_sold=is_sold,
#                                   description='Generic description', minimum_bid=min_bid, current_high_bid=high_bid,
#                                   image_link='Some link')


class TestBuyerNavigation(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_dashboard_loadsCorrectTemplate(self):
        dashboard = self.client.get('buyer/dashboard/')
        self.assertTrue(dashboard.status_code, 200)

    def test_category_loadsCorrectTemplate(self):
        category = self.client.get('buyer/dashboard/category/')
        self.assertTrue(category.status_code, 200)

    def test_product_loadsCorrectTemplate(self):
        product = self.client.get('buyer/dashboard/item/')
        self.assertTrue(product.status_code, 200)

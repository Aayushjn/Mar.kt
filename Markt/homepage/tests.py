from django.test import TestCase

from Markt.homepage.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1, name="User 1", email_id="user1@testemail.com", password="testpassword",
                            phone_number="1234567890", share_email=True, share_phone=False)

    def test_register(self):
        """TODO: test registration"""

    def test_login(self):
        """TODO: test login"""


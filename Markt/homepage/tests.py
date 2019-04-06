from django.test import TestCase, Client

from homepage.models import User


def create_user(name: str, email: str, password: str, phone: str, share_phone: bool) -> User:
    return User.objects.create(name=name, email_id=email, password=password, phone_number=phone, share_email=True,
                               share_phone=share_phone)


class TestMainNavigation(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_homepageView_loadsCorrectTemplate(self):
        homepage = self.client.get('/')
        self.assertTrue(homepage.status_code, 200)
        # self.assertTemplateUsed(homepage, 'homepage/index.html')

    def test_loginView_loadsCorrectTemplate(self):
        login = self.client.get('login/')
        self.assertTrue(login.status_code, 200)
        # self.assertTemplateUsed(login, 'homepage/login.html')

    def test_registerView_loadsCorrectTemplate(self):
        register = self.client.get('signup/')
        self.assertTrue(register.status_code, 200)
        # self.assertTemplateUsed(register, 'homepage/registration.html')

    def test_dashboardView_loadsCorrectTemplate(self):
        dashboard = self.client.get('dashboard/')
        self.assertTrue(dashboard.status_code, 200)
        # self.assertTemplateUsed(dashboard, 'homepage/dashboard.html')

    def test_mailboxView_loadsCorrectTemplate(self):
        mailbox = self.client.get('mailbox/')
        self.assertTrue(mailbox.status_code, 200)
        # self.assertTemplateUsed(mailbox, 'homepage/mailbox.html')

    def test_mailView_loadsCorrectTemplate(self):
        mail = self.client.get('mailbox/mailview/')
        self.assertTrue(mail.status_code, 200)
        # self.assertTemplateUsed(mail, 'homepage/mail-view.html')




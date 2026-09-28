from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AdminLoginFlowTests(TestCase):
    def test_admin_user_exists_and_can_login_to_admin_dashboard(self):
        User.objects.filter(username='admin').delete()
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': '123'})
        self.assertRedirects(response, reverse('admin_dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_default_customer_accounts_are_created(self):
        usernames = ['customer1', 'customer2', 'customer3']
        for username in usernames:
            User.objects.filter(username=username).delete()

        for username in usernames:
            User.objects.create_user(username=username, email=f'{username}@example.com', password='123456')

        for username in usernames:
            self.assertTrue(User.objects.filter(username=username).exists())

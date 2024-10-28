from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product
from user.models import User


class LoggingTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(name='admin', password='password', role='admin')
        self.product = Product.objects.create(
            title='Test Product',
            qty=10,
            price=100.00,
            description='Test Description'
        )

    def test_logging_product_addition(self):
        self.client.login(name='admin', password='password')
        response = self.client.post(reverse('add_product'), {
            'title': 'New Product',
            'qty': 20,
            'price': 200.00,
            'description': 'New Product Description'
        })
        self.assertEqual(response.status_code, 302)

        with open('app.log', 'r') as log_file:
            logs = log_file.readlines()

        self.assertTrue(any("Product added: New Product" in log for log in logs))


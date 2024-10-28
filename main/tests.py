import logging
import os
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from product.models import Product
from user.models import User


class ProductViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_admin = User.objects.create(name='admin', password='password', role='admin')
        self.test_manager = User.objects.create(name='manager', password='password', role='manager')
        self.test_user = User.objects.create(name='user', password='password', role='user')

        self.test_product = Product.objects.create(
            title='Test Product',
            qty=10,
            price=100.00,
            description='Test Description'
        )
        self.valid_data = {
            'title': 'New Product',
            'qty': 20,
            'price': 200.00,
            'description': 'New Product Description'
        }

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_product.title)
        logging.info('Product list view tested successfully.')

    def test_add_product_view(self):
        response = self.client.post(reverse('add_product'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirects
        self.assertTrue(Product.objects.filter(title='New Product').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product added successfully.")

        logging.info('Add product view tested successfully.')

    def test_update_product_view(self):
        updated_data = {
            'title': 'Updated Product',
            'qty': 15,
            'price': 150.00,
            'description': 'Updated Product Description'
        }
        response = self.client.post(reverse('update_product', args=[self.test_product.id]), data=updated_data)
        self.assertEqual(response.status_code, 302)
        self.test_product.refresh_from_db()
        self.assertEqual(self.test_product.title, 'Updated Product')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product updated successfully.")

        logging.info('Update product view tested successfully.')

    def test_delete_product_view(self):
        response = self.client.post(reverse('delete_product', args=[self.test_product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(id=self.test_product.id).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Product deleted successfully.")

        logging.info('Delete product view tested successfully.')

    def test_admin_dashboard_view_access(self):
        self.client.login(name='admin', password='password')
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_manager_dashboard_view_access(self):
        response = self.client.get(reverse('manager_dashboard'))
        self.assertEqual(response.status_code, 302)
        logging.info('Manager dashboard view tested successfully.')

    def test_user_dashboard_view_access(self):
        response = self.client.get(reverse('user_dashboard'))
        self.assertEqual(response.status_code, 302)
        logging.info('User dashboard view tested successfully.')

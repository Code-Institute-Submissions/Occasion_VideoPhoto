from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test.client import Client
from django.contrib.auth.decorators import login_required

# Create your tests here.


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test1')

    def testLogin(self):
        self.client.login(username='test123', password='test1')
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_get_products_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_details(self):
        product = Product.objects.create(description="test",
                                         things_include="test1", price=500)
        response = self.client.get(f'/products/{product.id}/')
        self.assertTemplateUsed(response, 'products/product_detail.html')

    @login_required
    def test_edit_product(self):
        product = Product.objects.create(description="test",
                                         things_include="test1", price=500)
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertTemplateUsed(response, 'products/edit_product.html')

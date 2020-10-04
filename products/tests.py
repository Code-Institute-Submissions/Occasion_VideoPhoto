from django.test import TestCase
from products.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import ProductForm
# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test1')

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
        response = self.client.post(f'/products/edit/{product.id}/',
                                    {'description': 'updated description'})
        self.assertRedirects(response, f'/accounts/login/?next=/products/edit/{product.id}/')
        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.description, 'test')

    def test_add_product(self):
        product = Product.objects.create(description="test",
                                         things_include="test1", price=500)
        response = self.client.post(f'/products/edit/{product.id}/')
        self.assertRedirects(response, f'/accounts/login/?next=/products/edit/{product.id}/')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')

    def test_category_string_method_returns_name(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

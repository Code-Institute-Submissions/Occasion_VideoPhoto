from django.test import TestCase
from products.models import Product, Package, Occasion

# Create your tests here.


class TestViews(TestCase):

    def test_get_bag_list(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_item_pag(self):
        id = 1
        response = self.client.post(f'/bag/add/ {id}')
        self.assertEqual(response.status_code, 301)

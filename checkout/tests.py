from django.test import TestCase
from .forms import OrderForm


class TestCheckoutForm(TestCase):

    def test_checkout_fullName_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    def test_street_address2_field_is_not_required(self):
        form = OrderForm({'full_name': 'Test','email':'test@hotmail.com',
                          'phone_number':'123','street_address1':'test',
                          'town_or_city':'test','country':'AA'})
        self.assertFalse(form.is_valid())

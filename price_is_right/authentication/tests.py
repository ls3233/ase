from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from models import User, UserProfile, ParentOrder


class ParentOrderTestCase(TestCase):
    def setUp(self):
        ParentOrder.objects.create(stock_name="ACME", is_sell=True, quantity=1000, success=False)
        ParentOrder.objects.create(stock_name="broken", is_sell=True, quantity=-1000, success=False)  # broken test, negative numbers not allowed

    def test_order_quantity_is_positive(self):
        working_order = ParentOrder.objects.get(stock_name="ACME")
        broken_order = ParentOrder.objects.get(stock_name="broken")
        self.assertTrue(working_order.valid_order())
        self.assertFalse(broken_order.valid_order())


from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    item = Menu.objects.create(
        title="IceCream", price=80, inventory=100)

    def test_get_item_title(self):
        self.assertEqual(self.item.title, "IceCream")

    def test_get_item_price(self):
        self.assertEqual(self.item.price, 80)

    def test_get_item_inventory(self):
        self.assertEqual(self.item.inventory, 100)

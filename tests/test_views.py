from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    Menu.objects.create(
        title="IceCream", price=80, inventory=100)
    Menu.objects.create(
        title="Toast", price=5, inventory=50)
    Menu.objects.create(
        title="Coffee", price=3, inventory=200)

    def test_getall(self):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer

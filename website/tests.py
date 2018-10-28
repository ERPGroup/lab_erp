from django.test import TestCase
from website.models import Category
# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name_category="Sach", quantity=2)
        

    def test_sach(self):
        sach = Category.objects.get(name_category="Sach")
        self.assertEqual(sach.quantity, 2)
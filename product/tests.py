from django.test import TestCase
from .models import Category

class TestCategory(TestCase):
    def test_category_creation(self):
        
        category = Category.objects.create(title="Livros", slug="livros")
        
        
        self.assertEqual(category.title, "Livros")
        self.assertEqual(category.slug, "livros")
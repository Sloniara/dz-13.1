import unittest
from main import Category, Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Electronics", "Products related to electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Products related to electronics")

    def test_product_initialization(self):
        product = Product("Laptop", "High-performance laptop", 1000, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "High-performance laptop")
        self.assertEqual(product.price, 1000)
        self.assertEqual(product.quantity_in_stock, 10)

    def test_count_products(self):
        category = Category("Electronics", "Products related to electronics")
        product1 = Product("Laptop", "High-performance laptop", 1000, 10)
        product2 = Product("Smartphone", "Latest smartphone model", 500, 20)
        category.add_product(product1)
        category.add_product(product2)
        self.assertEqual(len(category.products), 2)

    def test_count_categories(self):
        category1 = Category("Electronics", "Products related to electronics")
        category2 = Category("Clothing", "Fashionable clothing")
        self.assertEqual(Category.total_categories, 3)

if __name__ == '__main__':
    unittest.main()

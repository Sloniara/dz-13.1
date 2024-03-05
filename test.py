import pytest
from main import Category, Product

@pytest.fixture
def sample_category():
    return Category("Electronics", "Products related to electronics")

@pytest.fixture
def sample_product():
    return Product("Laptop", "High-performance laptop", 1000, 10)

def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Products related to electronics"

def test_product_initialization(sample_product):
    assert sample_product.name == "Laptop"
    assert sample_product.description == "High-performance laptop"
    assert sample_product.price == 1000
    assert sample_product.quantity_in_stock == 10

def test_count_products(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 1

def test_count_categories(sample_category):
    assert Category.total_categories == 3


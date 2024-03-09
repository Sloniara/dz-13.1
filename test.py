import pytest
from main import Category, Product

@pytest.fixture
def sample_category():
    return Category("Electronics", "Products related to electronics")

@pytest.fixture
def sample_product():
    return Product("Laptop", "High-performance laptop", 1000, 10)

def test_category_add_product(sample_category, sample_product):
    sample_category.add_product(sample_product)
    assert sample_category.get_products_info() == ["Laptop, 1000 руб. Остаток: 10 шт."]

def test_product_price_setter(sample_product):
    sample_product.price = 1500
    assert sample_product.price == 1500

def test_product_price_setter_incorrect_value(sample_product, capsys):
    sample_product.price = -500
    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена введена некорректно"
    assert sample_product.price == 1000  # Предполагается, что цена осталась без изменений

def test_product_price_deleter(sample_product, capsys):
    del sample_product.price
    captured = capsys.readouterr()
    assert captured.out.strip() == "Удаление атрибута 'price' не разрешено"
    assert hasattr(sample_product, "price")  # Предполагается, что атрибут 'price' не был удален


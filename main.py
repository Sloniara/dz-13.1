class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = [] if products is None else products
        Category.total_categories += 1
        Category.total_unique_products += len(set([product.name for product in self.products]))

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products = len(set([product.name for product in self.products]))


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
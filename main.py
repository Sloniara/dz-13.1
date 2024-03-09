class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут товаров
        Category.total_categories += 1

    def add_product(self, product):
        self.__products.append(product)

    def get_products_info(self):
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.")
        return products_info

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        return Product(name, description, price, quantity_in_stock)


class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity_in_stock = quantity_in_stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = value

    @price.deleter
    def price(self):
        print("Удаление атрибута 'price' не разрешено")

from src.products import Product

class Category:
    name: str
    description: str
    __products: list[Product]
    count_categories = 0
    count_products = 0

    def __init__(self, name, description, init_products):
        """Инициализация класса"""
        self.name = name
        self.description = description
        self.__products = init_products if init_products else []
        Category.count_categories += 1
        Category.count_products += len(self.__products)

    def add_product(self, product):
        """Добавление в класс Category списка продуктов """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.count_products += 1

    @property
    def get_products(self):
        return self.__products

    @property
    def products(self):
        product_strings = []
        for product in self.__products:
            product_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_strings)


# if __name__ == "__main__":
#     products = Product(
#     "Смартфоны",
#     "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#     "Samsung Galaxy C23 Ultra",
#     "121")
#
#     print(Category.description)
#     print(Category.name)
#     print(Category.products)

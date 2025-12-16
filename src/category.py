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

    def __str__(self):
        total_sum = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_sum} шт."


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
            product_strings.append(f"{str(product)}")
        return "\n".join(product_strings)

    def total_cost(self):
        total = 0
        for product in self.__products:
            total += product.price * product.quantity
        return total



# if __name__ == "__main__":
#     productss = Product(
#     "Смартфоны",
#     "Смартфоны",
#     111,
#     2)
#
#     productss2 = Product(
#     "Смартфоны",
#     "Смартфоны, как ",
#     222000,
#     2)
#
#     productss3 = Product(
#     "Смартфоны",
#     "Смартфоны, как средство жизни",
#     333000000,
#     2)
#
#
#
#     products = [productss, productss2, productss3]
#     total_cost = sum(product.price * product.quantity for product in products)
#     print(f"Общая стоимость товаров на складе: {total_cost} руб.")
#
#
#     print(total_cost)


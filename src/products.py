from typing import Optional


class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented

    @classmethod
    def new_product(cls, product: dict[str, str]) -> Optional["Product"]:
        return cls(
            name=product.get("name", ""),
            description=product.get("description", ""),
            price=product.get("price", 0),
            quantity=product.get("quantity", 0)
        )


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print(f"Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            say_new_price = input("Понизить цену товара? Введите 'у/n' если 'да/нет'.").lower()
            if say_new_price == "y":
                self.__price = new_price
        else:
            self.__price = new_price



# if __name__ == "__main__":
#     # product1 = {
#     #     "name": "Samsung Galaxy C23 Ultra",
#     #     "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#     #     "price": 30000,
#     #     "quantity": 121}
#     #
#     # product2 = Product.new_product(product1)
#     #
#     # product2.price = 1000
#     #
#     # print(product2)
#     # print("`~`" * 40)
#     # print(product2.name)
#     # print(product2.description)
#     # print(product2.price)
#
#     product1 = Product("Товар1", "Описание1", 10, 10)
#     product2 = Product("Товар2", "Описание2", 2, 2)
#
#     total_cost = product1 + product2
#     print(product1, product2, total_cost)
#     print("~"*50)
#     print(f"Общая стоимость товаров на складе: {total_cost} руб.")
#

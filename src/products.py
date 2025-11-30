class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == '__main__':
#
#     prod1 = Product("Samsung Galaxy C23 Ultra",
#                     "256GB, Серый цвет, 200MP камера",
#                     "180000.0",
#                     "5")
#
#     prod = Product("Банан", "Чтобы сесть", "123.12","1")
#     print(prod.name)
#     print(prod.description)
#     print(prod.price)
#     print("="*50)
#
#     print(prod1.name)
#     print(prod1.description)
#     print(prod1.price)
#     print(prod1.quantity)
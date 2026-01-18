from src.products import Product


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


# if __name__ == '__main__':
#     smartphone1 = Smartphone("Phone1", "Description1", 300, 10, "High", "ModelX", 128, "Black")
#     smartphone2 = Smartphone("Phone2", "Description2", 500, 5, "Medium", "ModelY", 256, "White")
#     lawn_grass1 = LawnGrass("Grass1", "Description1", 15, 20, "USA", 30, "Green")
#     lawn_grass2 = LawnGrass("Grass2", "Description2", 10, 25, "Canada", 35, "Green")
#
#     print(smartphone1 + smartphone2)  # Должно вывести 15
#     print(lawn_grass1 + lawn_grass2)  # Должно вывести 45
# print(lawn_grass1 + smartphone2)  # Ошибка

# Попробуй сложить разные типы, чтобы увидеть ошибку
# try:
#     print(smartphone1 + lawn_grass1)
# except TypeError:
#     print("TypeError: Нельзя складывать разные типы продуктов")

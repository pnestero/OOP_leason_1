from src.products import Product


class Category:
    name = str
    description = str
    products = list[Product]
    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_categories += 1
        Category.count_products += len(products) if products else 0


# if __name__ == "__main__":
#     prod1 = Product("Банан", "Чтобы сесть", "123.12", "1")
#     prod2 = Product("Ложка", "Чтобы есть", "10000", "20")
#
#     category = Category("banan", "sitdown", ["sss", "aaa", "ddd", "fjfdg"])
#
#     print(category.name)
#     print(category.description)
#     print(category.products)
#     print(len(category.products))
#     print("=" * 50)
#     print(category.count_products)
#     print(category.count_categories)
    # print(prod.name)
    # print(prod.description)
    # print(prod.price)
    # print(prod.quantity)

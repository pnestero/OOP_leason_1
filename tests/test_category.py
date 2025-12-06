from src.products import Product


def test_init_category(tests1_category):
    assert tests1_category.name == "Телевизор"
    assert tests1_category.description == "Samsung"
    assert tests1_category.count_categories == 1
    assert tests1_category.count_products == 1

def test_category_add_product(tests1_category):
    assert len(tests1_category.get_products) == 1
    tests1_category.add_product(Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2))
    assert len(tests1_category.get_products) == 2

def test_category_products(tests1_category):
    assert tests1_category.products == "Банан, 123.12 руб. Остаток: 2 шт."



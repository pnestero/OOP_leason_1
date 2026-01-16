from src.products import Product
# from

def test_init_category(tests1_category):
    assert tests1_category.name == "Телевизор"
    assert tests1_category.description == "Samsung"
    assert tests1_category.category_count == 1
    assert tests1_category.product_count == 1

def test_category_add_product(tests1_category):
    assert len(tests1_category.get_products) == 1
    tests1_category.add_product(Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2))
    assert len(tests1_category.get_products) == 2

def test_category_products(tests1_category):
    assert tests1_category.products == "Банан, 123.12 руб. Остаток: 2"

def test_str(tests1_category):
    assert str(tests1_category) == "Телевизор, количество продуктов: 2 шт."

def test_total_cost(tests1_category_total_cost):
    assert tests1_category_total_cost.total_cost() == 738.72

def test_average_price(tests1_category_average_price, tests2_category_average_price):
    assert tests1_category_average_price.average_price() == 123.12
    assert tests2_category_average_price.average_price() == 0.0


def test_custom_exception(capsys, tests1_category_average_price):
    assert len(tests1_category_average_price.get_products) == 1








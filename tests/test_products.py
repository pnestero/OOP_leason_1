from unittest.mock import patch

from src.products import Product


def test_product(tests1_product):
    assert tests1_product.name == "Банан"
    assert tests1_product.description == "Чтобы съесть"
    assert tests1_product.price == 123.12
    assert tests1_product.quantity == 2


def test_new_product():
    product1 = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "price": 30000,
        "quantity": 121}
    product = Product.new_product(product1)
    assert product.name == product1["name"]
    assert product.description == product1["description"]
    assert product.price == product1["price"]
    assert product.quantity == product1["quantity"]

def test_get_price(tests1_product):
    assert tests1_product.price == 123.12


def test_setter_price(tests1_product, capsys):
    tests1_product.price = 1000
    assert tests1_product.price == 1000

    tests1_product.price = -1
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"

def test_setter_price_y(tests1_product):
    with patch("builtins.input", return_value="y"):
        tests1_product.price = 100
        assert tests1_product.price == 100

def test_setter_price_n(tests1_product):
    with patch("builtins.input", return_value="n"):
        tests1_product.price = 100
        assert tests1_product.price == 123.12

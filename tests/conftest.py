import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def tests1_product():
    return Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2)

@pytest.fixture
def tests1_category():
    return Category(name="Телевизор",
                    description="Samsung",
                    init_products=[Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2)])


@pytest.fixture
def tests2_category():
    return Category(name="Телефон",
                    description="program developer",
                    products=[])
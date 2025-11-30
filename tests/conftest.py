import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def tests1_category():
    return Category(name="Телевизор",
                    description="Samsung",
                    products=["Kasper", "NLNK", "DDS"]
                    )

@pytest.fixture
def tests2_category():
    return Category(name="Телефон",
                    description="program developer",
                    products=["ICQ", "Vypres"]
                    )


@pytest.fixture
def tests1_product():
    return Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2)
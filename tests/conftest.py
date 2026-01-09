import pytest
from more_itertools.recipes import quantify

from src.category import Category
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone
from src.products import Product


@pytest.fixture
def tests1_product():
    return Product(name="Банан",
                   description="Чтобы съесть",
                   price=123.12,
                   quantity=2)


@pytest.fixture
def tests2_product():
    return Product(name="Чипсы",
                   description="Закуска",
                   price=200,
                   quantity=3)


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


@pytest.fixture
def tests1_category_total_cost():
    return Category(name="Телевизор",
                    description="Samsung",
                    init_products=[
                        Product(name="Банан",
                                description="Чтобы съесть",
                                price=123.12,
                                quantity=2),
                        Product(name="Банан",
                                description="Чтобы съесть",
                                price=123.12,
                                quantity=2),
                        Product(name="Банан",
                                description="Чтобы съесть",
                                price=123.12,
                                quantity=2)])

# Фикстуры для тестирования класса Smartphone
@pytest.fixture
def tests_smartphone_1():
    return Smartphone(name="Samsung Galaxy C23 Ultra",
                      description="256GB, Серый цвет, 200MP камера",
                      price=180000.0,
                      quantity=5,
                      efficiency=500,
                      model="Galaxy",
                      memory="16 GB",
                      color="red")

# Фикстуры для тестирования класса Smartphone
@pytest.fixture
def tests_smartphone_2():
    return Smartphone(name="IPhone",
                      description="512GB, Белый, 2000MP камера",
                      price=990000.0,
                      quantity=10,
                      efficiency=500,
                      model="IPhone",
                      memory="512GB",
                      color="Белый")

# Тестирование класса LawnGrass
@pytest.fixture
def tests_lawngrass_1():
    return LawnGrass(name="Газон многолетний",
                      description="Газон",
                      price=125,
                      quantity=99,
                      country="Rus",
                      germination_period="сентябрь",
                      color="Зеленый")

# Тестирование класса LawnGrass
@pytest.fixture
def tests_lawngrass_2():
    return LawnGrass(name="Газон на 1 год",
                      description="Газон",
                      price=100,
                      quantity=50,
                      country="Japan",
                      germination_period="май",
                      color="Светло-зеленый")
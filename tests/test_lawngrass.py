import pytest

def test_lawngrass_init(tests_lawngrass_1):
    """Инициализация класса"""
    assert tests_lawngrass_1.name == "Газон многолетний"
    assert tests_lawngrass_1.description == "Газон"
    assert tests_lawngrass_1.price == 125
    assert tests_lawngrass_1.quantity == 99
    assert tests_lawngrass_1.country == "Rus"
    assert tests_lawngrass_1.germination_period == "сентябрь"
    assert tests_lawngrass_1.color == "Зеленый"

def test_lawngrass_add(tests_lawngrass_1, tests_lawngrass_2):
    """Тестирование на сложение двух объектов класса"""
    assert tests_lawngrass_1 + tests_lawngrass_2 == 17375

def test_lawngrass_add_error(tests_lawngrass_1):
    with pytest.raises(TypeError):
        result = tests_lawngrass_1 + 1
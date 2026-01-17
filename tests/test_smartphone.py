import pytest

from src.smartphone import Smartphone


def test_smartphone_init(tests_smartphone_1):
    """Инициализация класса"""
    assert tests_smartphone_1.name == "Samsung Galaxy C23 Ultra"
    assert tests_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert tests_smartphone_1.price == 180000.0
    assert tests_smartphone_1.quantity == 5
    assert tests_smartphone_1.efficiency == 500
    assert tests_smartphone_1.model == "Galaxy"
    assert tests_smartphone_1.memory == "16 GB"
    assert tests_smartphone_1.color == "red"


def test_smartphone_add(tests_smartphone_1, tests_smartphone_2):
    """Сложение двух объектов класса"""
    assert tests_smartphone_1 + tests_smartphone_2 == 10800000


def test_smartphone_add_error(tests_smartphone_1, tests_smartphone_2):
    """Ошибка при сложении двух объектов класса"""
    with pytest.raises(TypeError):
        result = tests_smartphone_1 + 1

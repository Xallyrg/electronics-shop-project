"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_init():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_phone_number_of_sim_change():
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_phone_number_of_sim_change_raise_valueerror():
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_phone_init():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 1)"


def test_phone_add_item():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

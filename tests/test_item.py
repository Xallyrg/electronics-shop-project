"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
import pytest

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
item3 = Item("Смартфон", 10000, 20)
item4 = Item("Ноутбук", 20000, 5)


def test_init():
    assert item1.name == "Смартфон"
    assert item2.price == 20000
    assert item2.quantity == 5


def test_init_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_init_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item2.price == 20000
    assert item1.price == 8000


def test_init_name_change():
    assert item1.name == 'Смартфон'
    item1.name = 'New Name'
    assert item1.name == 'New Name'


def test_init_name_change_very_long():
    assert item1.name == 'New Name'
    item1.name = '012345678910111213'
    assert item1.name == '0123456789'


def test_init_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    # assert len(Item.all) == 9

    item1 = Item.all[2]
    assert item1.name == 'Смартфон'


def test_init_instantiate_from_csv_error_no_file():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/itemssss.csv')


def test_init_instantiate_from_csv_error_file_is_damaged():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/damaged_items.csv')


def test_init_string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number(5.5) == 5
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    # assert Item.string_to_number('5.5.1') == None
    # assert Item.string_to_number('asd') == None


def test_faild_to_convert_string_to_number():
    with pytest.raises(ValueError):
        Item.string_to_number('not a number')


def test_repr():
    assert repr(item3) == "Item('Смартфон', 10000, 20)"
    assert repr(item4) == "Item('Ноутбук', 20000, 5)"


def test_str():
    assert str(item3) == "Смартфон"
    assert str(item4) == "Ноутбук"


def test_add():
    assert item3 + item4 == 25


def test_add_raise_vallueerror():
    with pytest.raises(ValueError):
        item3 + 10

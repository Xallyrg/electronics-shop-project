"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


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
    assert len(Item.all) == 7

    item1 = Item.all[2]
    assert item1.name == 'Смартфон'


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
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"

def test_str():
    assert str(item1) == "Смартфон"
    assert str(item2) == "Ноутбук"


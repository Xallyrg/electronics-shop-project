"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
from src.item import Item
from src.keyboard import Keyboard
import pytest

keyboard1 = Keyboard('клава', 15000, 10)


def test_init():
    assert keyboard1.name == "клава"
    assert keyboard1.price == 15000
    assert keyboard1.quantity == 10
    assert keyboard1.language == 'EN'


def test_try_to_change_lang():
    with pytest.raises(AttributeError):
        keyboard1.language = 'eee'


def test_change_lang_by_method():
    assert keyboard1.language == 'EN'
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'

from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim
        self.all.append(self)

    @property
    def number_of_sim(self):
        '''
        позволяет смотреть на имя товара
        :return:
        '''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        '''
        позволяет менять имя товара. Обрезает его до 10 символов
        :return:
        '''
        if int(new_number_of_sim) == new_number_of_sim & new_number_of_sim > 0:
            self.__number_of_sim = new_number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


# смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# print(phone1)
# print(str(phone1))
# assert str(phone1) == 'iPhone 14'
# print(repr(phone1))
# assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
# assert phone1.number_of_sim == 2
#
# item1 = Item("Смартфон", 10000, 20)
# assert item1 + phone1 == 25
# assert phone1 + phone1 == 10
#
# print(phone1.number_of_sim)
# phone1.number_of_sim = 0
# print(phone1.number_of_sim)
# ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.

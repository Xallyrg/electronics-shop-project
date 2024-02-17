import csv


# def is_digit(string):
#     if string.isdigit():
#         return True
#     else:
#         try:
#             float(string)
#             return True
#         except ValueError:
#             return False


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        '''
        позволяет смотреть на имя товара
        :return:
        '''
        return self.__name

    @name.setter
    def name(self, new_name):
        '''
        позволяет менять имя товара. Обрезает его до 10 символов
        :return:
        '''
        if len(new_name) < 11:
            self.__name = new_name
        else:
            self.__name = new_name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
            Применяет установленную скидку для конкретного товара.
            """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        '''
        Достает данные из файла и создает товары по этим данным
        :param path:
        :return:
        '''
        list_of_items = []
        with open(path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                name = row['name']
                price = Item.string_to_number(row['price'])
                quantity = Item.string_to_number(row['quantity'])
                i = cls(name, price, quantity)
                list_of_items.append(i)
        return list_of_items

    @staticmethod
    def string_to_number(number):
        """
        Превращает вход (если возможно) в число формата int
        :param number:
        :return:
        """
        if isinstance(number, int) or isinstance(number, float):
            return int(number)
        # elif isinstance(number, str) and is_digit(number):
        #     return int(float(number))
        else:
            return int(float(number))
            # print('Это не число')
            # return None


# assert Item.string_to_number(5) == 5
# assert Item.string_to_number(5.5) == 5
# assert Item.string_to_number('5') == 5
# assert Item.string_to_number('5.0') == 5
# assert Item.string_to_number('5.5') == 5
# assert Item.string_to_number('5.5.1') == None
# assert Item.string_to_number('asd') == None

# item1 = Item("Смартфон", 10000, 20)
# print(str(item1))
# assert repr(item1) == "Item('Смартфон', 10000, 20)"
# assert str(item1) == 'Смартфон'

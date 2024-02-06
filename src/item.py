def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
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
        pass

    @staticmethod
    def string_to_number(number):
        """
        Превращает вход (если возможно) в число формата int
        :param number:
        :return:
        """
        if isinstance(number, int) or isinstance(number, float):
            return int(number)
        elif isinstance(number, str) and is_digit(number):
            return int(float(number))
        else:
            print('Это не число')
            return None



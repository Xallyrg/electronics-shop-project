from src.item import Item


class MixinLanguage:

    def __init__(self, name, price, quantity, language='EN'):
        """
        Создает язык английский, пробрасывает остальное в инициализатор Item
        """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        '''
        позволяет смотреть на язык
        :return:
        '''
        return self.__language

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(MixinLanguage, Item):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: язык раскладки, возникает из мискина.
        """
        super().__init__(name, price, quantity)
        self.all.append(self)
#
# keyboard1 = Keyboard('клава', 15000, 10)
#
# print(keyboard1)
# print(keyboard1.__dict__)
# print(keyboard1.language)
#
# keyboard1.change_lang()
# print(keyboard1.language)
#
# keyboard1.change_lang()
# print(keyboard1.language)

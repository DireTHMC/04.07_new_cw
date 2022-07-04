def phonebook(name: str, number: str) -> str:
    normal_view = f'имя - {name}, номер - {number}\n'
    with open('text5.txt', 'a+', encoding="utf8") as f:
        print(f.write(normal_view))
    return 'Saved!'


class Hero:
    MIN_COORD = 0
    MAX_COORD = 10

    def __init__(self, power, chakra):
        self.__power = power
        self.__chakra = chakra

    def __str__(self):
        return f'Класс для создания героев'

    def get_status(self):
        return f'сила'

    def get_hp(self):

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def calc(x, y):
        return x + y


elem = Hero(111, 200)

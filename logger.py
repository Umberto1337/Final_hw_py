import logging
import argparse

logging.basicConfig(filename='all.log', filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


# region Task_1 Rectangle
class NegativeValueError(ValueError):
    pass


class Rectangle:
    """
    Создаёт треуголник позволяет работать с ним

    """

    # region field
    def __init__(self, width, height=0):

        if width.isdigit():
            width = int(width)
            height = int(height)

            if width >= 0 and height >= 0:
                self._width = width
                if height == 0:
                    self._height = width
                else:
                    self._height = height
                logger.info(f'Create Rectangel({self.width}, {self.height})')
            else:
                if width <= 0:
                    logger.error(NegativeValueError(f'Ширина должна быть положительной, а не {width}'))
                elif height <= 0:
                    logger.error(NegativeValueError(f'Высота должна быть положительной, а не {height}'))

        else:
            logger.error(ValueError("Введёны некоректные данные"))


    # endregion

    # region decorator
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            logger.error(NegativeValueError(f'Ширина должна быть положительной, а не {value}'))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            logger.error(NegativeValueError(f'Высота должна быть положительной, а не {value}'))

    # endregion

    # region method
    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    # endregion


def parse():
    parser = argparse.ArgumentParser(
        description='Создаём Трекгольник логируем созданный треугольник',
        epilog='При отрецательный значениях логируем исключение',
        prog='Rectangle()')
    parser.add_argument('-w', '--width', help='Какая ширина у треугольника : ')
    parser.add_argument('-hi', '--height', default=0, help='Какая высота у треугольника : ')
    args = parser.parse_args()
    return Rectangle(args.width,
                     args.height)


#
#
# if __name__ == '__main__':
#     # r1 = Rectangle(-7)
#     # r2 = Rectangle(5)
#     # r3 = Rectangle(4, -5)
#     print(parse())

# endregion

# region Task 2 Persone


class NegativeAge(ValueError):
    pass


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        if age > 0:
            self._age = age
            logger.info(f'Сотрудник {self.first_name} возраст {self._age} внесён в базу данных')
        else:
            logger.error(NegativeValueError(f'Введён некорректный возрас {age}'))

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def parse():
    parser = argparse.ArgumentParser(
        description='Записываем сотрудника в базу данных',
        epilog='При отрецательном значение возраста логируем ошибку',
        prog='Employee()')

    parser.add_argument('-ln', '--lastname', help='Фамилия сотрудника : ')
    parser.add_argument('-n', '--name', help='Имя сторудника : ')
    parser.add_argument('-pa', '--patronymic', help='Отчество Сотрудника : ')
    parser.add_argument('-ag', '--age', help='Возраст сотрудника : ')
    parser.add_argument('-po', '--position', help='Должность сотрудника : ')
    parser.add_argument('-sa', '--salary', help='Зарплата сотрудника : ')
    args = parser.parse_args()

    return Employee(args.lastname,
                    args.name,
                    args.patronymic,
                    int(args.age),
                    args.position,
                    args.salary)

# if __name__ == '__main__':

# person_1 = Employee('Zuev',
#                     'Alexey',
#                     'Olegovich',
#                     36,
#                     'developer',
#                     5.500)
#
# person_2 = Employee('Bad',
#                     'Persone',
#                     ' ',
#                     0,
#                     'bad',
#                     0.0)

# print(parse())

# endregion
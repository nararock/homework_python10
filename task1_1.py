class PositiveInteger:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Количество клеток не должно быть отрицательным.")
        elif not isinstance(value, int):
            raise ValueError("Количество клеток должно быть целым числом.")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Cell:
    quantity = PositiveInteger()

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        print(f"Сумма клеток равна {self.quantity + other.quantity}")
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            print(f"Разность клеток равна {self.quantity - other.quantity}")
            return Cell(self.quantity - other.quantity)
        else:
            print("Разность количества ячеек двух клеток меньше нуля!")

    def __mul__(self, other):
        print(f"Произведение клеток равно {self.quantity * other.quantity}")
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        print(f"Частное клеток равно {self.quantity // other.quantity}")
        return Cell(self.quantity // other.quantity)


# print("Проверка на отрицательное значение")
# cell1 = Cell(-30)
# print("Проверка на целые значения")
# cell2 = Cell(30.2)


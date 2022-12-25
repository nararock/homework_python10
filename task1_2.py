import numbers


class MatrixDescr:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        cm = CheckMatrix(value)
        if not isinstance(value, list):
            raise TypeError("Данные должны быть списком.")
        elif len(value) == 0:
            raise ValueError("Список не должен быть пустым.")
        elif not cm.check_two_Dim():
            raise TypeError("Данные должны быть двумерным списком.")
        elif not cm.check_numbers():
            raise TypeError("Список должен состоять из чисел.")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


"""
класс CheckMatrix создан для вызова проверочных функций
"""


class CheckMatrix:
    def __init__(self, check_matrix):
        self.check_matrix = check_matrix

    def check_two_Dim(self):
        for i in range(len(self.check_matrix)):
            if not isinstance(self.check_matrix[i], list):
                return False
        return True

    def check_numbers(self):
        for i in range(len(self.check_matrix)):
            for j in range(len(self.check_matrix[i])):
                if not isinstance(self.check_matrix[i][j], numbers.Number):
                    return False
        return True


class Matrix:
    matrix = MatrixDescr()

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        new_str = ""
        for el in self.matrix:
            for i in el:
                new_str += str(i) + " "
            new_str += "\n"
        return new_str

    def __add__(self, other):
        answer = []
        for el in range(len(self.matrix)):
            answer.append([])
            for i in range(len(self.matrix[0])):
                answer[el].append(self.matrix[el][i] + other.matrix[el][i])
        return Matrix(answer)


# print("Проверка на список")
# m1 = Matrix((1, 2))
# print("Проверка на пустой список")
# m2 = Matrix([])
# print("Проверка на список списков")
# m3 = Matrix([1, 3, 6])
# print("Проверка на числа в списке")
# m4 = Matrix([[1, 4], ['k', 0]])

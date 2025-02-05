from typing import List
import copy


class Quadrilateral:
    color = "Неопределённый"  # Статическое поле, общее для всех четырехугольников

    def __init__(self, sides=None, color="Неопределённый"):
        if sides is None:
            self.sides = [1.0, 1.0, 1.0, 1.0]  # Стороны по умолчанию
        else:
            if len(sides) != 4:
                raise ValueError("Четырёхугольник должен иметь ровно четыре стороны.")
            self.sides = sides  # Динамическое поле
        self.color = color
        print(f"Четырёхугольник создан с сторонами {self.sides} и цветом {self.color}")

    # Конструктор копирования
    @classmethod
    def from_quadrilateral(cls, other):
        return cls(copy.deepcopy(other.sides), other.color)

    def __del__(self):
        print(f"Четырёхугольник со сторонами {self.sides} уничтожается.")

    # Перегрузка Метода 1: Принимает список сторон
    def set_sides(self, sides: List[float]):
        if len(sides) != 4:
            raise ValueError("Требуются ровно четыре стороны.")
        self.sides = sides
        print(f"Стороны четырехугольника установлены на {self.sides}")

    # Перегрузка Метода 2: Принимает четыре отдельные стороны
    def set_sides_overload(self, side1: float, side2: float, side3: float, side4: float):
        self.sides = [side1, side2, side3, side4]
        print(f"Стороны четырехугольника установлены на {self.sides}")

    # Константный метод: Не изменяет объект
    def get_perimeter(self) -> float:
        perimeter = sum(self.sides)
        print(f"Вычисление периметра: {perimeter}")
        return perimeter

    # Приватный метод
    def _validate_sides(self) -> bool:
        # Простая проверка: все стороны должны быть положительными
        valid = all(side > 0 for side in self.sides)
        print(f"Проверка сторон {self.sides}: {'Валидные' if valid else 'Невалидные'}")
        return valid

    # Метод, вызывающий приватный метод
    def process_sides(self):
        if self._validate_sides():
            print("Стороны валидны. Обработка сторон.")
        else:
            print("Невалидные стороны. Обработка невозможна.")

    # Функциональный метод: вывод информации
    def print_info(self):
        print(f"Четырёхугольник - Стороны: {self.sides}, Цвет: {self.color}")

    # Функциональный метод: вычисление площади (для переопределения)
    def calculate_area(self) -> float:
        print("Вычисление площади для общего четырехугольника.")
        # Заглушка
        return 0.0


class Rectangle(Quadrilateral):
    rectangle_count = 0  # Статическое поле

    def __init__(self, length=1.0, breadth=1.0, color="Неопределённый"):
        super().__init__([length, breadth, length, breadth], color)
        self.length = length  # Динамическое поле
        self.breadth = breadth  # Динамическое поле
        Rectangle.rectangle_count += 1
        print(f"Прямоугольник создан. Всего прямоугольников: {Rectangle.rectangle_count}")

    def __del__(self):
        Rectangle.rectangle_count -= 1
        print(f"Прямоугольник уничтожен. Осталось прямоугольников: {Rectangle.rectangle_count}")
        super().__del__()

    # Переопределение calculate_area
    def calculate_area(self) -> float:
        area = self.length * self.breadth
        print(f"Вычисление площади Прямоугольника: {self.length} * {self.breadth} = {area}")
        return area

    # Переопределение print_info
    def print_info(self):
        print(f"Прямоугольник - Длина: {self.length}, Ширина: {self.breadth}, Цвет: {self.color}")

    # Геттер и Сеттер для длины
    def get_length(self) -> float:
        return self.length

    def set_length(self, length: float):
        if length > 0:
            self.length = length
            self.sides = [self.length, self.breadth, self.length, self.breadth]
            print(f"Длина прямоугольника установлена на {self.length}")
        else:
            print("Длина должна быть положительной.")

    # Геттер и Сеттер для ширины
    def get_breadth(self) -> float:
        return self.breadth

    def set_breadth(self, breadth: float):
        if breadth > 0:
            self.breadth = breadth
            self.sides = [self.length, self.breadth, self.length, self.breadth]
            print(f"Ширина прямоугольника установлена на {self.breadth}")
        else:
            print("Ширина должна быть положительной.")


class Parallelogram(Quadrilateral):
    _parallelogram_count = 0  # Статическое поле, защищённое

    def __init__(self, base=1.0, height=1.0, color="Неопределённый"):
        super().__init__([base, height, base, height], color)
        self.base = base  # Динамическое поле
        self.height = height  # Динамическое поле
        Parallelogram._parallelogram_count += 1
        print(f"Параллелограмм создан. Всего параллелограммов: {Parallelogram._parallelogram_count}")

    def __del__(self):
        Parallelogram._parallelogram_count -= 1
        print(f"Параллелограмм уничтожен. Осталось параллелограммов: {Parallelogram._parallelogram_count}")
        super().__del__()

    # Переопределение calculate_area
    def calculate_area(self) -> float:
        area = self.base * self.height
        print(f"Вычисление площади Параллелограмма: {self.base} * {self.height} = {area}")
        return area

    # Переопределение print_info
    def print_info(self):
        print(f"Параллелограмм - Основание: {self.base}, Высота: {self.height}, Цвет: {self.color}")

    # Геттер и Сеттер для основания
    def get_base(self) -> float:
        return self.base

    def set_base(self, base: float):
        if base > 0:
            self.base = base
            self.sides = [self.base, self.height, self.base, self.height]
            print(f"Основание параллелограмма установлено на {self.base}")
        else:
            print("Основание должно быть положительным.")

    # Геттер и Сеттер для высоты
    def get_height(self) -> float:
        return self.height

    def set_height(self, height: float):
        if height > 0:
            self.height = height
            self.sides = [self.base, self.height, self.base, self.height]
            print(f"Высота параллелограмма установлена на {self.height}")
        else:
            print("Высота должна быть положительной.")


class Square(Rectangle):
    square_count = 0  # Статическое поле

    def __init__(self, side=1.0, color="Неопределённый"):
        super().__init__(length=side, breadth=side, color=color)
        self.side = side  # Динамическое поле
        Square.square_count += 1
        print(f"Квадрат создан. Всего квадратов: {Square.square_count}")

    def __del__(self):
        Square.square_count -= 1
        print(f"Квадрат уничтожен. Осталось квадратов: {Square.square_count}")
        super().__del__()

    # Переопределение calculate_area
    def calculate_area(self) -> float:
        area = self.side ** 2
        print(f"Вычисление площади Квадрата: {self.side}^2 = {area}")
        return area

    # Переопределение print_info
    def print_info(self):
        print(f"Квадрат - Сторона: {self.side}, Цвет: {self.color}")

    # Геттер и Сеттер для стороны
    def get_side(self) -> float:
        return self.side

    def set_side(self, side: float):
        if side > 0:
            self.side = side
            self.length = side
            self.breadth = side
            self.sides = [side, side, side, side]
            print(f"Сторона квадрата установлена на {self.side}")
        else:
            print("Сторона должна быть положительной.")


def main_menu():
    # Общий список для демонстрации полиморфизма
    all_quadrilaterals: List[Quadrilateral] = []

    while True:
        print("\n--- Меню Управления Четырехугольниками ---")
        print("1. Создать Четырёхугольник")
        print("2. Создать Прямоугольник")
        print("3. Создать Параллелограмм")
        print("4. Создать Квадрат")
        print("5. Вывести Все Объекты")
        print("6. Вычислить Площади (Полиморфизм)")
        print("7. Вычислить Периметры")
        print("8. Вывести Информацию об Объекте")
        print("9. Обработать Стороны")
        print("10. Демонстрация Полиморфизма")
        print("0. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            try:
                sides_input = input("Введите четыре стороны через пробел: ")
                sides = list(map(float, sides_input.strip().split()))
                color = input("Введите цвет: ")
                quad = Quadrilateral(sides, color)
                all_quadrilaterals.append(quad)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            try:
                length = float(input("Введите длину: "))
                breadth = float(input("Введите ширину: "))
                color = input("Введите цвет: ")
                rect = Rectangle(length, breadth, color)
                all_quadrilaterals.append(rect)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == "3":
            try:
                base = float(input("Введите основание: "))
                height = float(input("Введите высоту: "))
                color = input("Введите цвет: ")
                para = Parallelogram(base, height, color)
                all_quadrilaterals.append(para)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовые значения.")

        elif choice == "4":
            try:
                side = float(input("Введите длину стороны: "))
                color = input("Введите цвет: ")
                sq = Square(side, color)
                all_quadrilaterals.append(sq)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовое значение.")

        elif choice == "5":
            print("\n-- Все Четырёхугольники --")
            for idx, quad in enumerate(all_quadrilaterals, 1):
                print(f"{idx}. {quad}")

        elif choice == "6":
            print("\n-- Вычисление Площадей (Полиморфизм) --")
            for quad in all_quadrilaterals:
                quad.calculate_area()

        elif choice == "7":
            print("\n-- Вычисление Периметров --")
            for quad in all_quadrilaterals:
                perimeter = quad.get_perimeter()
                print(f"Периметр: {perimeter}")

        elif choice == "8":
            print("\n-- Информация об Объектах --")
            for idx, quad in enumerate(all_quadrilaterals, 1):
                print(f"{idx}. ", end="")
                quad.print_info()

        elif choice == "9":
            print("\n-- Обработка Сторон --")
            for quad in all_quadrilaterals:
                quad.process_sides()

        elif choice == "10":
            # Демонстрация полиморфизма
            print("\n--- Демонстрация Полиморфизма ---")
            for quad in all_quadrilaterals:
                print("--------")
                quad.print_info()
                area = quad.calculate_area()
                perimeter = quad.get_perimeter()
                print(f"Площадь: {area}")
                print(f"Периметр: {perimeter}")
            print("--------")

        elif choice == "0":
            print("Завершение программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите действительный вариант.")


if __name__ == "__main__":
    main_menu()

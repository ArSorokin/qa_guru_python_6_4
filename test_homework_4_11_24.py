import math, random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # сосчитайте периметр
    perimeter = (a * 2) + (b * 2)
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # сосчитайте площадь
    area = math.pi * r ** 2
    pi = 3.14
    assert area == 1661.9025137490005

    # сосчитайте длину окружности
    length = math.pi * 2 * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # создайте список
    l = []
    amount = len(l)

    # Решение сходу:
    while amount < 10:
        l.append(random.randint(1, 100))
        amount = len(l)

    # Подсмотрел в test_homework.py
    # n = 10
    # l = [random.randint(1, 100) for i in range(n)]

    print("\nUnsorted:", l)
    l.sort()
    print("Sorted:", l)

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # удалите повторяющиеся элементы

    print("\n", l, sep="")
    l = list(set(l))
    print(l)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # создайте словарь
    # d = {}
    d = dict(zip(first, second))
    # print(d.values())
    # print(list(d.items()))
    # print(list(d.keys()))
    print("\n", list(d.values()), sep="")

    assert isinstance(d, dict)
    assert len(d) == 5
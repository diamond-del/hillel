from typing import List

# func 1
str1 = input("Введите строку 1: ")
str2 = input("Введите строку 2: ")


def is_str_bigger(str1: str, str2: str) -> str:
    """
    В этой функции проверяется,
    какая строка больше,
    c помощью len,
    и возвращает ту строку, которая длиннее
    """
    if len(str1) > len(str2):
        return str1
    else:
        return str2


print(is_str_bigger(str1, str2))

# func 2

your_input = input("Введите числа или буквы через пробел: ")
list1 = your_input.split()  # Превращаем строку в список, ну чтобы заданию соотвествовать


def is_list_digit(lst: List[str]) -> bool:
    """
    В данной функции проверяется каждый
    элемент списка, цифра ли это или нет,
    и эта функция возвращает True, если да,
    и False, если нет
    """
    for item in lst:
        if not item.isdigit():
            return False
    return True


print(is_list_digit(list1))

# func 3


def print_smth(str: str) -> str:
    """
    Это простейшая функция из всех трех,
    просто выводит в терминал символы,
    ничего не возвращая
    """
    print(str)


print(print_smth("'*' * 80"))

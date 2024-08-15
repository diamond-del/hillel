# func 1
# str1 = input("Введите строку 1: ")
# str2 = input("Введите строку 2: ")
#
#
# def is_str_bigger(str1: str, str2: str) -> str:
#     if len(str1) > len(str2):
#         return "Строка 1 больше строки 2"
#     else:
#         return "Строка 2 больше строки 1"


# print(is_str_bigger(str1, str2))

# func 2
# from typing import List
#
# your_input = input("Введите числа или буквы через пробел: ")
# list1 = your_input.split()
#
# def is_list_digit(lst: List[str]) -> bool:
#     for item in lst:
#         if not item.isdigit():
#             return False
#     return True

# print(is_list_digit(list1))

# func 3


def print_smth(str: str) -> str:
    print(str)


print_smth("'*' * 80")

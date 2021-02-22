"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(num_list: list) -> None:
    """
          Checking the number from list for repetition
    """
    passed_values = set()
    for element in num_list:
        if element in passed_values:
            print('Yes', end=' ')
        else:
            print('No', end=' ')
            passed_values.add(element)


check_list = [1, 2, 3, 5, 1, 5, 9, 2, 7, 4, 1, 0, 8, 3]
yes_or_no(check_list)

# expected result: No No No No Yes Yes No Yes No No Yes No No Yes

"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(num_list: list) -> None:
    new_list = []
    for num in num_list:
        if num in new_list:
            print('Yes')
        else:
            print('No')
        new_list.append(num)


check_list = [1, 2, 3, 5, 1, 5, 9, 2, 7, 4, 1, 0, 8, 3]

yes_or_no(check_list)

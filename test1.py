"""
Написать генератор get_even_number, который возвращает подряд четные числа
Например:
even_gen = get_even_number()
next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(even=2):
    while True:
        yield even
        even += 2


even_gen = get_even_number()
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))

"""
Написать генератор get_even_number, который возвращает подряд четные числа
Например:
even_gen = get_even_number()
next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""
from typing import Generator


def get_even_number() -> Generator[int, None, None]:
    """
        Generate even numbers, start from 2
    """
    even = 2
    while True:
        yield even
        even += 2


if __name__ == "__main__":
    even_gen = get_even_number()
    assert next(even_gen) == 2
    assert next(even_gen) == 4
    assert next(even_gen) == 6
    print('tests passed!')

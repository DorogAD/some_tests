"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет результат сложения цифр целого числа
"""


def num_sum(numb: int) -> int:
    result = 0
    for element in str(numb):
        result += int(element)
    return result


if __name__ == '__main__':
    assert num_sum(5216) == 14
    print('Решено!')

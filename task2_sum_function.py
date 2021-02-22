"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет результат сложения цифр целого числа
"""


def num_sum(numb: int) -> int:
    """
        Calculating sum of number's digits
    """
    result = 0
    for element in str(numb):
        result += int(element)
    return result


if __name__ == '__main__':
    assert num_sum(5216) == 14
    print('Решено!')


def num_sum2(numb: int) -> int:
    """
        Calculating sum of number's digits
    """
    result = 0
    while numb:
        result += numb % 10
        numb = numb // 10
    return result


if __name__ == '__main__':
    assert num_sum2(5216) == 14
    print('Решено!')

"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Определить атрибуты:
- value - текущее значение счетчика
Определить методы:
- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:

    def __init__(self, value: int = 0) -> None:
        self.value = value

    def __iter__(self) -> object:
        return self

    def __next__(self) -> int:
        value = self.value
        self.value += 1
        return value

    def increase(self, num: int = 1):
        self.value += num
        return self.value

    def decrease(self, num: int = 1):
        self.value -= num
        return self.value


if __name__ == '__main__':
    x = Counter()
    assert next(x) == 0
    assert next(x) == 1
    assert next(x) == 2
    assert x.increase(10) == 13
    assert x.decrease(5) == 8
    print('Решено!')

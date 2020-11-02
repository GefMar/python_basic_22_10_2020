# homework lesson: 3, task:1
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

import random

data = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(100000)]


def division(a: float, b: float) -> float:
    """
    делит а на b
    :param a:
    :param b:
    :return: float or None
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        return float('nan')


result = []
for itm in data:
    result.append(division(*itm))

test = list(map(lambda x: x ** 2, result))
division2 = lambda a, b: a / b if b else float('nan')

assert division(4, 2) == 2, 'division(4, 2) SOME TEXT'
assert division(14, 2) == 7, 'division(14, 2)'
assert division(0, 2) == 0, 'division(0, 2)'
assert division(-22, 4) == -5.5, 'division(-22, 4)'
assert division(1, 0) * 0, 'division(1, 0)'

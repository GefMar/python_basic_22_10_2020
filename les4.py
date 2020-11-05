import os
import sys
from time import sleep, time
import random
import datetime as dt

# def sleep(a):
#     print(f'IM SLEEP {a} sec')
#
#
# _, str_date = sys.argv
#
# b_date = dt.datetime.strptime(str_date, "%d.%m.%Y")
#
# age = dt.datetime.now().year - b_date.year
# print(age)
#

# a = [1, 2, 3, 4, 5, 5, 3, 1]

# b = {idx: itm for idx, itm in enumerate(a) if itm & 1}
#
# for itm in a:
#     if itm & 1:
#         for x in range(10):
#             b.append((itm, x))
#
#
# def log(funk):
#
#     def wrap(*args, **kwargs):
#         print(dt.datetime.now(), funk.__name__)
#         start = time()
#         result = funk(*args, **kwargs)
#         print(dt.datetime.now(), 'END WORK', funk.__name__)
#         print(time() - start)
#         return result
#
#     return wrap
#
#
# @log
# def some_a(x, y):
#     return x + y
#
#
# @log
# def some_b(x, y, z):
#     return (x * y) ** z
#
#
# # some_a = log(some_a)
# # some_b = log(some_b)
#
# print(some_a(1, 2))
# print(some_b(2, 3, 5))

print(os.listdir())

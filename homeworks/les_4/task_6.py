from itertools import cycle


def int_iter(n):
    while True:
        yield n
        n += 1


def my_cycle(iter_object):
    idx = 0
    len_iter = len(iter_object)
    while True:
        yield iter_object[idx]
        idx = idx + 1 if idx < len_iter else 0

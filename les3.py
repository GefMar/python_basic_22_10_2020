"""
 если желаете использовать функцию из этого списка, надо написать ее аналог
sum()
map()
reduce()
min()
max()
enumerate()
zip()
"""


def my_sum(a: float, b: float) -> float:
    """My sum func for two elements
    :param a int or float digit
    :param b int or float digit
    :return sum a b
    """
    result = a + b
    return result


def some(a: int) -> int:
    return a ** 3


def my_map(funk, iter_obj):
    print('f 1')
    for itm in iter_obj:
        print('f 2')
        yield funk(itm)
        print('f 3')
        yield itm + 5
    yield 'SOME VAR'
    print('f 4')


def some_two(one, two, three, *, four=1):
    return f'{one}, {two}, {three}, {four}'


def some_three(name, surname):
    return f'fullname: {name} {surname}'


def some_four(a, b, *args, **kwargs):
    print(type(args))
    print(kwargs)
    print(a)
    print(b)
    return sum(args)


some_list = [1, 2, 34, 5, 6]


def some_five():
    global some_list
    some_list = []
    some_list.append('HELLOOOOOO')
    def some():
        return ''
    return some


c = some_five(some_list)
print(c)
print(some_list)
print(c is some_list)

user = {
    'name': 'Sergey',
    'surname': 'Romanchuk'
}

# c = some_three(**user)
# c = some_four(1, 2, 3, 4, 5, 6, 7, 8, some=23, arrr='ffgjfgjf')
# print(c)


#
# b = my_map(some, [1, 2, 3, 4, 5])
# while True:
#     try:
#         itm = next(b)
#         print(itm)
#     except StopIteration:
#         break

# for itm in my_map(some, [1, 2, 3, 4, 5]):
#     print(itm)
#     if itm > 125:
#         break

def while_test(n):
    result = []
    idx = 0
    while idx < n:
        result.append(idx)
        idx += 1


def for_test(n):
    result = []
    for idx in range(n):
        result.append(idx)


# while_test(10**5)
for_test(10**5)

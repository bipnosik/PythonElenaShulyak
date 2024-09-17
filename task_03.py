def max_odd(array):
    result = None
    for x in array:
        if isinstance(x, (float,int)) and x % 2 != 0:
            x = int(x)
            if result is None or x > result:
                result = x

    return result


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))

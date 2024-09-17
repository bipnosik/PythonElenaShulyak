def coincidence(list1=None, range1=None):
    if list1 is None or range1 is None:
        return []

    result = []
    for x in list1:
        if isinstance(x, (int, float)) and range1.start <= x < range1.stop:
            result.append(x)

    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))

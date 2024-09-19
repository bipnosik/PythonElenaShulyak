def sort_list(list1):
    if not list1:
        return []

    max_num = max(list1)
    min_num = min(list1)
    result = [max_num if x == min_num else min_num if x == max_num else x for x in list1]

    result.append(min_num)
    return result
print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))








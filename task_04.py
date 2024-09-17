def sort_list(list1):
    if not list1:
        return []

    max_num = max(list1)
    min_num = min(list1)
    max_numindex = list1.index(max_num)
    min_numindex = list1.index(min_num)

    list1[max_numindex],list1[min_numindex]  = min_num,max_num
    list1.append(min_num)
    return list1

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))







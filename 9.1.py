def connect_dicts(dict1, dict2):

    merged_dict = {}


    sum_dict1 = sum(value for value in dict1.values())
    sum_dict2 = sum(value for value in dict2.values())


    for key, value in sorted(dict1.items(), key=lambda x: x[1], reverse=True):
        if value >= 10:
            merged_dict[key] = value
    for key, value in sorted(dict2.items(), key=lambda x: x[1], reverse=True):
        if value >= 10 and (key not in merged_dict or sum_dict2 >= sum_dict1):
            merged_dict[key] = value

    return dict(sorted(merged_dict.items(), key=lambda x: x[1]))

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))




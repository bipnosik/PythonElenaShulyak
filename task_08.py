import re

def multiply_numbers(inputs):


    if not isinstance(inputs, str):
        inputs = str(inputs)


    cleaned_string = re.sub(r'[^0-9]', '', inputs)

    if not cleaned_string:
        return None


    result = 1

    for digit in map(int, cleaned_string):
        result *= digit

    return result

print(multiply_numbers(None))
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))









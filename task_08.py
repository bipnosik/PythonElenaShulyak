def multiply_numbers(inputs):
    if isinstance(inputs, str):
        digits = [int(d) for d in inputs if d.isdigit()]
        if digits:
            return multiply(digits)
        else:
            return None
    elif isinstance(inputs, (int, float)):
        return multiply_numbers(str(inputs))
    elif isinstance(inputs, (list, tuple)):
        return multiply(inputs)
    else:
        return None

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_numbers(None))
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))









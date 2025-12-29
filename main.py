def even_numbers_sum(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total = total + n
    return total
print(even_numbers_sum([1, 2, 3, 4, 5]))
def even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
print(even_numbers([1, 2, 3, 4, 5]))
def double_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n * 2)
    return result
print(double_numbers([1, 2, 3, 4, 5]))

def new_list(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n * 2)
    return result
print(new_list([1, 2, 3, 4, 5]))
# Transform List
def square_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result
print(square_numbers([1, 2, 3, 4]))

# Filter List
def get_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result
print(get_even_numbers([1, 2, 3, 4, 5, 6]))

# Aggregate / Sum
def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(sum_numbers([1, 2, 3, 4]))

# Filter + Transform
def double_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n * 2)
    return result
print(double_even_numbers([1, 2, 3, 4, 5, 6]))

# Count Items
def count_even_numbers(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count
print(count_even_numbers([1, 2, 3, 4, 5, 6, 8]))

# Find first Match
def first_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None
print(first_first_even([1, 3, 5, 7, 8]))

# Dictionary Count
def count_words(words):
    result = {}
    for w in words:
        if w not in result:
            result[w] = 1
        else:
            result[w] += 1
    return result
print(count_words(["error", "info", "error", "warn", "info"]))

# Loop Dictionary
log_counts = count_words((["error", "info", "error", "warn"]))
for level, count in log_counts.items():
    print(level, count)


def is_multiple(possibleMultiple, number):
    return number % possibleMultiple == 0


print(is_multiple(5, 10))  # true
print(is_multiple(5, 12))  # false
print(is_multiple(5, 15))  # true

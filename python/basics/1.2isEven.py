# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators

def is_even(num):
    # ends with 0,2,4,6,8
    return num & 1 == 0


print(is_even(0))
print(is_even(10))
print(is_even(-11))

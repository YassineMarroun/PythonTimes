"""
Algorithm to determine if a string has all unique characters.
"""

unique_str = "AbCdEfG"
non_unique_str = "non Unique STR"


def normalize(input_str):
    input_str = input_str.replace(" ", "")
    return input_str.lower()


def is_unique1(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


def is_unique2(input_str):
    return len(input_str) == len(set(input_str))


def is_unique3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True


unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(unique_str)
print(non_unique_str)

print(is_unique1(unique_str))
print(is_unique1(non_unique_str))

print(is_unique2(unique_str))
print(is_unique2(non_unique_str))

print(is_unique3(unique_str))
print(is_unique3(non_unique_str))

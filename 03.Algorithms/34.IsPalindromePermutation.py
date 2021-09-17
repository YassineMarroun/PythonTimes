"""
Given a string, a function to check  if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome
does not need to be limited to just dictionary words.
"""

pal_perm = "Tact Coa"  # Taco Cat
not_pal_perm = "This is not a palindrome permutation"


def is_pal_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True


print(is_pal_perm(pal_perm))
print(is_pal_perm(not_pal_perm))

"""
Given a string, function to determine if it is a palindrome.
"""

# racecar
# madam
# Dammit I'm mad.


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
        return True


str_1 = "racecar"
str_2 = "Dammit I'm mad."
str_3 = "Computer"

print(is_palindrome(str_1))
print(is_palindrome(str_2))
print(is_palindrome(str_3))

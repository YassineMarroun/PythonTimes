# Given a string, count the number of consonants.

input_str_1 = "abcd de"
input_str_2 = "VisualStudioCode"

vowels = "aeiou"


def iterative_count_consonants(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            count += 1
    return count


def recursive_count_consonants(input_str):

    if input_str == '':
        return 0
    
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(iterative_count_consonants(input_str_1))
print(iterative_count_consonants(input_str_2))

print(recursive_count_consonants(input_str_1))
print(recursive_count_consonants(input_str_2))
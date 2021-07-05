def generate_pairs(limit):
    num = 1
    new_list = []

    while num < limit:
        new_list.append(num * 2)
        num = num + 1

    return new_list


print(generate_pairs(10))


# Using yield
def generate_pairs2(limit):
    num = 1

    while num < limit:
        yield num * 2
        num = num + 1


returnPairs = generate_pairs2(10)
print(next(returnPairs))
print("Here is more code")
print(next(returnPairs))
print("Here is more code")
print(next(returnPairs))


def return_cities(*cities):
    for element in cities:
        # for subElement in element:
        yield from element


returned_cities = return_cities("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(returned_cities))
print(next(returned_cities))

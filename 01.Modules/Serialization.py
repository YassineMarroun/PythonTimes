import pickle

"""
name_list = ["Peter", "Marc", "Michael", "Jhon"]

binary_file = open("name_list", "wb")
pickle.dump(name_list, binary_file)
binary_file.close()

del binary_file
"""

file = open("name_list", "rb")

n_list = pickle.load(file)
print(n_list)

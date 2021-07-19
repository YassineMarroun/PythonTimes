from io import open

"""
text_file = open("file.txt, "w")
sentence = "Great day to study Python\n on Wednesday"
text_file.write(sentence
text_file.close()
"""


"""
text_file = open("file.txt", "r")

text = text_file.read()
# text_lines = text_file.readlines()
text_file.close()

print(text)
# print(text_lines[0])
"""


"""
text_file = open("file.txt", "a")
text_file.write("\nIt is always a good time to study Python")
text_file.close()
"""


"""
text_file = open("file.txt", "r")
print(text_file.read())
print("-------------------------")
text_file.seek(10)
print(text_file.read())
print("-------------------------")
text_file.seek(len(text_file.read())/2)
print(text_file.read())
"""


text_file = open("file.txt", "r+")  # Reading and writing
text_file.write("Beginning of the text")
print(text_file.readlines())
print("-------------------------")
text_file.seek(0)
text_list = text_file.readlines()
text_list[1] = "This line has been included from outside\n"
text_file.seek(0)
text_file.writelines(text_list)
text_file.close()

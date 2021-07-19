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

text_file = open("file.txt", "a")
text_file.write("\n It is always a good time to study Python")
text_file.close()

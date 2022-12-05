my_text="This text is a test"
result=my_text[0]
print(result)
result=my_text[7]
print(result)
result=my_text[-3]
print(result)
result=my_text.index("h")
print(result)

my_text="This text is a test"
result=my_text.index("s")
print(result)

my_text="This text is a test"
result=my_text.index("s",5)
print(result)

# my_text="This text is a test"
# result=my_text.index("s",5,11) #ValueError
# print(result)

# result=my_text.index("q")#ValueError
# print(result)
result=my_text.index("text")
print(result)
# result=my_text.index("H")#ValueError
# print(result)

my_text="This text is a test"
result=my_text.rindex("s")
print(result)


# practise
# Find and display on the screen which character occupies the fifth position within the following word:
# "computer"
word = "computer"
print(word[4])

# Find and display the index of the first occurrence of the word "practice" in the following sentence:
#
#
#
# "In theory, theory and practice are the same. In practice, they are not."

sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.index("practice"))

# Find and display the index of the last occurrence of the word "practice" in the following sentence:
#
#
#
# "In theory, theory and practice are the same. In practice, they are not."
sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.rindex("practice"))





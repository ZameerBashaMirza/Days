text= "We are going to learn six methods today"
# result=text
# print(result)
#
# result=text.upper()
# print(result)
#
# result=text.upper
# print(result)

result=text[4].index("r")
print(result)

result=text.lower()
print(result)

result=text.split()
print(result)

result=text.split("o")
print(result)

a="learning"
b="Python"
c="is"
d="amazing"
e=" ".join([a,b,c,d])
print(e)

a="learning"
b="Python"
c="is"
d="amazing"
e="-".join([a,b,c,d])
print(e)

text= "We are going to learn six methods today"
result=text.find("q")
print(result)#-1

text= "We are going to learn six methods today"
result=text.replace("six","a lot of ")
print(result)

text= "We are going to learn six methods today"
result=text.replace("e","x")
print(result)

# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
text="Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence=text.upper()
print(sentence)

# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.

word_list = ["Simple","is","better","than","complex."]
x=" ".join(word_list)
print(x)
"""
Replace in the following sentence:
"If the implementation is hard to explain, it might be a bad idea."
the following pairs of words:
"hard" --> "easy"
"bad" --> "good"
and display the sentence with both words modified.
"""
string="If the implementation is hard to explain, it might be a bad idea."
result=string.replace("hard","easy").replace("bad","good")
print(result)

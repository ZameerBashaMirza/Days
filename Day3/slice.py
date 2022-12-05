text="ABCDEFGHIJKLM"
fragment=text[2]
print(fragment)
fragment=text[2:5]
print(fragment)
fragment=text[2:]
print(fragment)
fragment=text[:5]
print(fragment)
fragment=text[2:10:2]
print(fragment)
fragment=text[2:10:3]
print(fragment)
fragment=text[::3]
print(fragment)
fragment=text[::-2]
print(fragment)
fragment=text[::-2]
print(fragment)

# Extract the first word of the following sentence using slicing, and display it on the screen:
#
#
#
# "Controlling complexity is the essence of programming"

sentence = "Controlling complexity is the essence of programming"
print(sentence[0:11])

# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"

sentence = "Never trust a computer you can't throw out a window"
print(sentence[8::3])
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"

sentence = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print(sentence[::-1])


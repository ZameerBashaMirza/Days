'''
ask user enter text?
enter 3 random letters
1--how many times appear each of those letters
upper and lower--
2--how many words in total?
3-first & last letters?
4-words in inverted order
5-is python there

booleans,dic,

'''
text=input("Please enter any text?:  ")


# rand_letters1,rand_letters2,rand_letters3=input("enter 3 random letters?   ")#SMD
"""a1=rand_letters1,rand_letters2,rand_letters3
print(a1.count(rand_letters1))
print(a1.count(rand_letters2))
print(a1.count(rand_letters3))

lenth=len(a1)
print(lenth)"""
list_letters=[]
list_letters.append(input("enter 1 random letters?").lower())
list_letters.append(input("enter 1 random letters?").lower())
list_letters.append(input("enter 1 random letters?").lower())
print(list_letters)
first= list_letters.count(list_letters[0])
second= list_letters.count(list_letters[1])
third= list_letters.count(list_letters[2])

print(f"{list_letters[0]}:{first} times")
print(f"{list_letters[1]}:{second} times")
print(f"{list_letters[2]}:{third} times")

text_partition=text.split()
print(text_partition)
word_f=len(text_partition)
print(word_f)

text_words=" ".join(text_partition)
print(text_words)
print(len(text_words))
print(f"first_letter: {text_words[0]} and last_letter: {text_words[-1]}")

print('python'in text)

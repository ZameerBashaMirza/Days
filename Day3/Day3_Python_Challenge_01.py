text=input("Enter a text of your choice: ")
letters =[]
text = text.lower()
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the first letter: ").lower())

print("\n")
print("LETTER REPETITIONS")
letters_repetition1=text.count(letters[0])
letters_repetition2=text.count(letters[1])
letters_repetition3=text.count(letters[2])

print(f" We have found the letter {letters[0]} repeated {letters_repetition1} times")
print(f" We have found the letter {letters[1]} repeated {letters_repetition2} times")
print(f" We have found the letter {letters[2]} repeated {letters_repetition3} times")

print("\n")
print("NUMBER OF WORDS")

words=text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTERS")

first_letter=text[0]
last_letter=text[-1]
print(f"The inital letter: '{first_letter}', the final letter is '{last_letter}")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text=' '.join(words)
print(f" if we oreder your text backwards it will say '{inverted_text}")

print("\n")
print("LOOKING FOR THE WORD PYTHON")

is_python ='python' in text
dic={True:'was',False: 'was not'}

print(f"The word 'Python' {dic[is_python]}found in the text")





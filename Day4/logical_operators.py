4<5
5<6
my_bool=4<5<6
print(my_bool)

my_bool=4<5>6
print(my_bool)

my_bool=4<5 and 5>6
print(my_bool)

my_bool=(4<5) and (5==2+3)
print(my_bool)

my_bool=(55==55)and ('dog'=='dog')
print(my_bool)

my_bool=10==10 or 3==3
print(my_bool)

my_bool=1==10 or 3==30
print(my_bool)


text='This sentence is short'
my_bool='sentence' in text
print(my_bool)

text='This sentence is short'
my_bool=('sentence' in text) or ('python' in text)
print(my_bool)

my_bool='a'=='a'
print(my_bool)

my_bool=not'a'=='a'
print(my_bool)

my_bool=not'a'!='a'
print(my_bool)

"""
Create three variables (num1, num2, and num3):

Inside num1, store the value 36

Inside num2, stores the result of the operation 72/2

Inside num3, store the value 48

Check if num1 is greater than num2, and less than num3. 
Store the result of that comparison in a variable called my_bool.
"""
num1=36
num2=72/2
num3=48
my_bool=(num1>num2) and (num2<num3)
print(my_bool)

"""
Create three variables (num1, num2, and num3):

Inside num1, store the value 36

Inside num2, stores the result of the operation 72/2

Inside num3, store the value 48

Check if num1 is greater than num2, or less than num3. 
Store the result of that comparison in a variable called my_bool.
"""
num1=36
num2=72/2
num3=48
my_bool=(num1>num2)or (num2<num3)
print(my_bool)

"""
Check if the words:

word1 = "success", and

word2 = "technology"

are not found in the sentence below, 
and store the result (a boolean) in a variable called my_bool:

"When something is important enough, 
you do it even if the odds are against you" - Elon Musk"""

sentence="When something is important enough, you do it even if the odds are against you"
word1="success"
word2="technology"
my_bool=(not word1 in sentence)and (not word2 in sentence)
print(my_bool)











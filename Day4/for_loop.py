my_list=['a','b','c','d']
for letter in my_list:
    print(letter)

my_list=['a','b','c','d']
for letter in my_list:
    print("letter:"+letter)

my_list=['a','b','c','d']
for letter in my_list:
    letter_number=my_list.index(letter)+1
    print(f"letter {letter_number}: {letter}")

my_list=["Paul",'Laura',"Fede","Louis",'Julia']
for name in my_list:
    if name.startswith('L'):
        print(name)

my_list=["Paul",'Laura',"Fede","Louis",'Julia']
for name in my_list:
    if name.startswith('L'):
        print(name)
    else:
        print("This name does not begin with 'L")

numbers=[1,2,3,4,5]
my_value=0

for number in numbers:
    my_value=my_value+number
print(my_value)

numbers=[1,2,3,4,5]
my_value=0

for number in numbers:
    my_value=my_value+number
    print(my_value)

word='python'
for letter in word:
    print(letter)

for letter in (1,2,3):
    print(letter)

for object in [[1, 2], [3, 4], [5, 6]]:
    print(object)

for a,b in [[1, 2], [3, 4], [5, 6]]:
     print(a)
     print(b)

for a,b in [[1, 2], [3, 4], [5, 6]]:
     print(a)


dic={
    'key1':'a',
    'key2':'b',
    'key3':'c'
}
for item in dic:
    print(item)

dic={
    'key1':'a',
    'key2':'b',
    'key3':'c'
}
for a,b in dic.items():
    print(a,b)

for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for item in dic.keys():
    print(item)

"""Practice #1
Using For loops, greet all members of a class, printing "Hello" + their name.

For example: "Hello Norville

students = ["Norville", "Fred", "Velma", "Daphne"]
"""
students = ["Norville", "Fred", "Velma", "Daphne"]
for student in students:
    print(f"Hello {student}")


"""Practice #2
Given the following list of numbers, 
calculate the sum of all the numbers using For loops and store 
the result of the sum in a variable called sum_numbers:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
"""
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_numbers = 0
for number in list_numbers:
    sum_numbers=sum_numbers+number
print(sum_numbers)

"""
Practice #3
Given the following list of numbers,
 perform the sum of all even and odd* numbers separately 
 in the variables sum_even and sum_odd respectively:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recall from previous days: the modulus (or remainder) of a number 
divided by 2 is zero when said value is even, and 1 when it is odd

num % 2 == 0 (even values)

num % 2 == 1 (odd values)
"""
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for number in list_numbers:
    if number%2==0:
        sum_even=sum_even+number
    else:
        sum_odd=sum_odd+number
print(sum_even)
print(sum_odd)

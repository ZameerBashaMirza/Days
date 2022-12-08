# coins=5
# while coins>0:
#     print(f"I have{coins} coins")
#     coins=coins-1
#
# coins=5
# while coins>0:
#     print(f"I have{coins} coins")
#     coins-=1
#
# coins=5
# while coins>0:
#     print(f"I have{coins} coins")
#     coins-=1
# else:
#     print("I have no money anymore")
#
#
# answer='y'
# while answer=='y':
#     answer=input("do you want to continue(y/n)")
# else:
#     print("Thank you")
#
# """answer='y'
# while answer=='y':
#     pass
# print("Hello")"""
#
# name=input("Your name:")
# for letter in name:
#     print(letter)
#
# name=input("Your name:")
# for letter in name:
#     if letter =='r':
#         break
#     print(letter)
#
#
# name=input("Your name:")
# for letter in name:
#     if letter =='r':
#         continue
#     print(letter)
"""
While Loops Practice #1
Create a While Loop that prints the numbers 10 to 0 on the screen, one at a time.
"""
number = 10
while number>=0:
    print(number)
    number-=1

"""
While Loops Practice #2
Create a While Loop that subtracts one by one the numbers from 50 to 0
 (both numbers included) with the following additional conditions:

If the number is divisible by 5, show that number on the screen 
(remember that here you can use the modulus operation 
dividing by 5 and checking the remainder!)

If the number is not divisible by 5, continue executing the loop
 without showing the value on the screen 
 (don't forget to continue subtracting so that the program doesn't run infinitely).
"""
number = 50
while number>=0:
    if number%5==0:
        print(number)
    number-=1


list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for number in list_numbers:
    if number>0:
        print(number)


print('%'*20)
"""
Loop Interruption Statements Practice
Create a For loop through the following list of numbers, 
printing each of its elements to the screen, 
and interrupt the flow when you find a negative value:

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
"""

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for n in list_numbers:
    if n>=0:
        print(n)
    else:
        break

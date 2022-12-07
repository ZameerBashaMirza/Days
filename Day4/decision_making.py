if 10>9:
    print("It is correct")

if True:
    print("It is correct")

x=True
if x:
    print("It is correct")

if 5==2:
    print("It is wrong")

if 5==2:
    print("It is correct")
else:
    print("It is not correct")

pet='dog'
if pet=='cat':
    print("You have a cat")
elif pet=='dog':
    print("You have a dog")
elif pet=='fish':
    print("You have a fish")
else:
    print("I don't know what animal you have")


age=16

if age<18:
    print("You are a minor")
else:
    print("You are a adult")

age=16
school_grade=9

if age<18:
    print("you are a minor")
    if school_grade>=7:
        print("Passed")
    else:
        print("Failed")
else:
    print("You are an adult")

"""
Using the variables num1 and num2,
which are fed with user input (just like in the provided code),
create a flow control structure that compares the values of the variables,
and returns a result according to the case:

"num1 is greater than num2"

"num2 is greater than num1"

"num1 and num2 are equal"

You must display the value of the user input instead of num1 and num2.
"""
num1 = input("Enter a number:")
num2 = input("Enter another number:")

if num1==num2:
    print(f"{num1} and {num2} are equal")
elif num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")

"""
The laws of a certain country establish that 
an adult can drive if they are of legal age (18 years or older), and have a driver's license.

Create a conditional structure to check if a 16-year-old without a license can drive, 
and display the corresponding result on the screen:

"You can drive"

"You can't drive yet. You must be 18 years old and have a license"

"You can't drive. You need to have a license"

Use the code base already provided to set up the appropriate 
flow control structure and check those conditions.
"""
age = 18
has_license = False
if age>=18:
    if has_license==True:
        print("You can drive")
    else:
        print("You can't drive. You need to have a license")
else:
    print("You can't drive yet. You must be 18 years old and have a license")

"""
To access a certain job, the candidate must be able to program in Python and speak French.

Create a conditional structure to evaluate a candidate given these conditions, 
and display the corresponding message on the screen:

"You meet the requirements to apply"

"To apply, you need to know how to program in Python and speak French"

"To apply, you need to speak French"

"To apply, you need to know how to program in Python"

Use the code already provided to set up the appropriate flow control structure
 and check those conditions. Evaluate a candidate who knows French,
  but does not know how to program in Python.
"""

speak_french =True
knows_python =False

if speak_french and knows_python:
    print("You meet the requirements to apply")
elif not speak_french and not knows_python:
    print("To apply, you need to know how to program in Python and speak French")
elif not speak_french:
        print("To apply, you need to speak French")
elif not knows_python:
        print("To apply, you need to know how to program in Python")
























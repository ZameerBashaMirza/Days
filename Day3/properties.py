"""
name="Harry"

name[0]='G'
print(name)# TypeError: 'str' object does not support item assignment
"""
name="Harry"
name="Garry"
print(name)

n1="Ga"
n2="rry"
print(n1+n2)

n1="Ga"
n2="rry"
print(n1*10)

poem="""Thousand little white fish as if boiled 
the color of the water
  """
print("water" in poem)
print("sun" in poem)

# Practice
# Concatenate the text "Repetition" 15 times and display the result on the screen.
print("Repetition"*15)

"""
Check if the word "beach" is not found in the following haiku. You should print the boolean.

"Whitecaps on the bay:

A broken signboard banging

In the April wind."

— Richard Wright, collected in Haiku: This Other World, 1998
"""
haiku="""
Whitecaps on the bay:

A broken signboard banging

In the April wind.
"""
print("beach" not in haiku)
"""
Check the Python Documentation to find the description of the len() function.
 Then, display on the screen the length (in number of characters) of the word
  electroencephalographist.
"""
print(len("electroencephalographist"))

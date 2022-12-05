text= "We are going to learn six methods today"
result=text
print(result)

result=text.upper()
print(result)

result=text.upper
print(result)

result=text[4].upper()
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


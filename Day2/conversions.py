num1=20
num2=30.5

num1=num1+num2
print(type(num1))
print(type(num2))

num1=5.8
print(num1)
print(type(num1))

num2=int(num1)
print(num2)
print(type(num1))
print(type(num2))

age=input("Tell me your age: ")

print(type(age))
age=int(age)
print(age)
print(type(age))
new_age=1+age
print(new_age)
# print("YOur new age is going to be " + new_age)#TypeError: can only concatenate str (not "int") to str

num1=7.5
result=int(num1)
print(type(result))

# num2=7
# result1=float(num2)
# print(type(result1))

num1="7.5"
num2="10"
print(float(num1)+int(num2))

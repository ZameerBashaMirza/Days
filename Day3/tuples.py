my_tuples=(1,2,3,4)
print(my_tuples)

my_tuples1=1,2,3,4
print(my_tuples1)

print(my_tuples[0])
print(my_tuples[-1])
'''
my_tuples[0]=5
print(my_tuples)#TypeError: 'tuple' object does not support item assignment
'''

my_tuples=(1,2,(10,20),4)
print(my_tuples[2][0])

my_tuples=list(my_tuples)
print(my_tuples)

my_tuples=tuple(my_tuples)
print(type(my_tuples))

t=(1,2,3)
x,y,z=t
print(x,y,z)
'''
t=(1,2,3)
x,z=t
print(x,y,z)#ValueError: too many values to unpack (expected 2)
'''
print('A'*10)
t1=(1,2,3,1)
print(t1)
print(t1.index(2))
# print(t1.index(0))#ValueError: tuple.index(x): x not in tuple
# print(t1.index(1))
# print(t1.index(3))
print(len(t1))
print(t1)
print(t1.count((1)))

# practice
'''
Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
'''
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(my_tuple.count(2))

'''
Convert the following tuple to a list, and store it in a variable called my_list.
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
'''
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
my_list=list(my_tuple)
print(my_list.count(2))

'''
Extract the elements of the following tuple into four variables: a, b, c, d

my_tuple = (1, 2, 3, 4)
'''
my_tuple = (1, 2, 3, 4)
a,b,c,d=my_tuple

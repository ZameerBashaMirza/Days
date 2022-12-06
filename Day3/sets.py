my_set=set([1,2,3,4,5])
print(my_set)

print(type(my_set))
'''
my_set=set(1,2,3,4,5)#TypeError: set expected at most 1 argument, got 5
print(my_set)

print(type(my_set))
'''
'''
other_set={1,2,3}
print(other_set)
print(type(other_set))
'''
'''
my_set=set([1,2,3,4,5])
print(type(my_set))
print(my_set[0])#TypeError: 'set' object is not subscriptable
'''

# list and dictionaries are not included

# my_set=set((1,2,3,1,2,3,[1,2]))
# print(my_set)

my_set=set((1,2,3,4,5))
print(2 in my_set)
print(len(my_set))

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
s4=s1|s2
print(s4)
print(s3)

s1.add(4)
print(s1)
s1.add(2)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
s2.discard(6)#if it is available then remove otherwise it shows no error
print(s2)
# s2.remove(6)#KeyError: 6
print(s2)



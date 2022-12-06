# my_list=['a','b','c']
# another_list=['hello',55,6.1]
# result=len(my_list)
# print(another_list)
# print(type(another_list))
# print(result)
# print(type(my_list))
#
# result1=my_list[0]
# print(result1)
# result2=my_list[0:2]
# print(result2)
#
# my_list3=['d','e','f']
# print(my_list+my_list3)
# my_list3[0]='Alpha'
# print(my_list3)
# my_list3.append('g')
# print(my_list3)
#
# my_list3.pop()
# print(my_list3)

list1=['g','o','b','m','c']
new_list=list1.sort()
print(new_list)#None
print(type(new_list))#NoneType

list2=['g','o','b','m','c']
list2.sort()
print(list2)
list2.reverse()
print(list2)


# Create a list with 5 elements, inside the variable my_list. You can include strings, booleans, numbers, etc.
my_list=["Hello",True,55,5.6,["Hello",True,55,5.6]]
print(my_list)

# Add the element "motorcycle" to the following list of means of transportation:
# transportation_means = ["plane", "car", "ship", "bicycle"]
transportation_means = ["plane", "car", "ship", "bicycle"]
transportation_means.append("motorcycle")
print(transportation_means)
"""
Use the pop() method to remove the third item from the following list called fruits, and store it in a variable called deleted_item. Use list methods without altering the line of code already supplied.

apple

banana

mango

cherry

watermelon
"""

fruits = ["apple", "banana", "mango", "cherry", "watermelon"]
deleted_item=fruits.pop(2)
print(fruits)
print(deleted_item)
my_dictionary={'c1':'value1','c2':'value2'}
print(type(my_dictionary))
print(my_dictionary)

result=my_dictionary['c1']
print(result)

result=my_dictionary['c2']
print(result)

customer={
    'name':'John',
    'last_name':"Lennon",
    'weight':88,
    'height':1.76
}
query=(customer['last_name'])
print(query)

query=(customer['height'])
print(query)

dict={
    1:55,
    2:[10,20,30],
    3:{'s1':100, 's2':200}

}
print(dict[2])
print(dict[2][1])
print(dict[3])
print(dict[3]['s2'])



dic={
    'k1':['a','b''c'],
    'k2':['d','e','f']

}
print(dic['k2'][1].upper())
print(dic['k1'][0].upper())


dic={1:'a',2:'b'}
print(dic)
dic[3]='c'
print(dic)


dic[2]='B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

# practice
"""
Create a dictionary called my_dict that stores the following information about a person:

name: Karen

surname: Jurgens

age: 35

occupation: Journalist

The names of the keys and values must be equal to the ones indicated above.
"""
my_dict={
    'name':"Karen",
    'surname':'Jurgens',
    'age':35,
    'occupation':'Journalist'
}
print(my_dict)

'''
Use print to returns the second item of the list called points2, inside the following dictionary.

If the value 300 were to change in the future,
 the code should work the same to return the value at that same position. 
 To do this, you must refer to the names of the keys and/or indexes as appropriate.
'''
my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict['points']['points2'][1]) #Use dictionary indices to extract the second item of points2
'''
Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:

name: Karen

surname: Jurgens

age: 36

occupation: Editor

country: Colombia

to do this, you should not change the line of code already written, 
but update the values using dictionary methods.
'''
my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict['age']=36
my_dict['occupation']='Editor'
my_dict['country']='Colombia'

print(my_dict)























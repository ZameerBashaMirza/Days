#format function

x=10
y=5
print("my numbers are " +str(x)+" and "+str(y))

print("My numbers are {} and {}".format(x,y))

print("The sum of {} and {} is equal  to  {}".format(y,x,y+x))

#formatted string literals
color="red"
license_plate=541926
print(f"The car is {color} and its license plate is {license_plate}.")

associate_name = "Jesse Pinkman"
associate_number = 399058

print(f"Dear {(associate_name)}, your associate number is: {(associate_number)}".format(associate_name,associate_number))

new_points = 350
total_points = 1225
print(f"\"You have earned ({new_points}) points! In total, you have accumulated ({total_points}) points\"".format(new_points,total_points))

new_points = 350
total_points = 1225
print(f"\"You have earned ({new_points}) points! In total, you have accumulated ({total_points}) points\"".format(new_points,total_points))

previous_points = 875
new_points = 350
total_points=previous_points+new_points
print(f"\"You have earned ({new_points}) points! In total, you have accumulated ({total_points}) points\"")
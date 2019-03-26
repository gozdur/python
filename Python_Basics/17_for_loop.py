# For loops
#for loop will refer to a variable which will contain diffrent data every time the loop loops
# for loop can be applied agains a string dictionary, array, tuple,

friends = ["jim", "carren", "kevin"]


for my_var in "juniper":  # iterates trough a string and prints each character
    print(my_var)

print("\n")

for my_var2 in friends: # iterates trough an array (list) and prints every value
    print(my_var2)

print("\n")

for my_var3 in range(10):   # will print out the index of 10 from zero to 9 not including 10
    print(my_var3)

for my_var4 in range(len(friends)):  # will print out the the frinds with index 0 1 2 cause we are passing a 3 in range cause the array happens to have 3 fields
    print(friends[my_var4])


for my_var5 in range(len(friends)):
    if my_var5 == 0:
        print("First iteration")
    else:
        print("Not first")
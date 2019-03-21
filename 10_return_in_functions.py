
# return statement returns the output of the function, otherwise print
# stetement would give none, when we use return it records the output

def cube(num):
    return num*num*num

print(cube(4))


# This fucntion returns the value of the function stores it in a variable and
# than the variable is printed as a float number

def add(num):
    return num+num


result = add(3)
print (float(result))
### Basic Numbers in Python

print("Basic printing of numbers")
print(2) # prints a number
print(2.1) # prints a decimal number
print (-2) # prints a negative number

# Basic Arithmetic

print("Basic arithmetic")
print(2 + 2) # adds two numbers
print(2 + 2.2) # adds two numbers one is decimal
print(2 * 2) # multiplies two numbers
print(2 * 2) # divides two numbers
print(2 ** 4) # exponents of number
print(2 * 4 + 4) # standard order of operation
print(2 * (4 + 4)) # order of operation enforced by parentheses ()
print(10 % 3) # a mod n in math which gives a reminder like:  dividend a | n divisor


# Store numbers in variables

my_var = -5
my_var2 = 4
my_var3 = 7

print(my_var) # prints the variable my_var which is a integer (liczba calkowita)

# using str function that converts numbers in to a string

print(str(my_var2)) # str function that converts a number is to a string usefull when printing numbers
print(str(my_var3) + " is my favourite number")

# Common math functions that are used in Python

print(abs(my_var)) # abs function that checks what is the absolute value of a number ( absolute value of -5 is 5)
print(pow(2, 3)) # pow function does value to the power of value (value, value)
print(max(4, 6)) # checks which number is larger and prints it or stores it
print(max(2, my_var)) # a variable can also be used as a function parameter
print(min(4, 5)) # checks which number is smaller and prints it or takes it
print(round(4.7)) # rounds number to the closest integer (liczba calkowita)
print(round(4.5)) # rounds number to the closest integer (liczba calkowita)

from math import *  # calls math module and imports all functions

print(floor(7.8)) # floor function (from math module) rounds down number all the time
print(ceil(7.8)) # floor function (from math module) rounds down number all the time
print(sqrt(9))
# gives a quare root of a number
print(sqrt(my_var2)) # gives a quare root of a number (pierwiastek)



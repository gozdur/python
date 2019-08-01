# Program asks user for a number and prints out if the numer is odd or even.

number = int(input("Please provide a number: "))

value = number % 2

if value == 0:
    print("The number is even")
else:
    print("The number is odd")
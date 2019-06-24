
# Variable my_var is a user input converted to string
# FOr as long as entered value is a valid integer it will be ok
# if the user will enter letters the program will stop

#   number_var = int(input("Enter a number: "))
#   print(number_var)

print("\n")

# Code with expect error handling:


try:
    number_var2 = int(input("Enter a number: "))
    print(number_var2)
    division = 10 / 0   # div
    # Dision by zero is not allowed but it will be included in the try statement and except clause will run agains this is not optimal
except ZeroDivisionError as err_var: # this is a specific return error for division by zero in Python
    print(err_var) # we can stor an arror in a variable using the "as" operator in above line
except ValueError: # This error type is for wrong values
    print("Invalid input")



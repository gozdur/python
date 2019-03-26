
num1 = input("Please provide first number:")
num2 = input("Plase provide second number:")

result = num1 + num2

print("\n""This result will be bad because user input is a string")

print(result)  # result is bad cause the user input is a string by default


# We need to convert the string from the user to the numbers

print("\n""This result will be good cause we converted string to integer with int function""\n""But decimal point numbers still dont work")

# int function converts the variable to an integer (liczba calkowita)

#result2 = int(num1) + int(num2)
#print(result2)

print("\n" "This time this will be correct also for float numbers")

# float function converts the number to float type (dziesietna z przecinkiem)

result3 = float(num1) + float(num2)
print(result3)


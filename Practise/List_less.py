# This program checks numbers in a list and prints out all numbers that are < 5
# Also takes that number which fullfils that condition and puts number in a new list
# Later user inputs a number and the original list is checked agoins that number

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

for number in a:
    if number <= 5:
        print(number)
        x.append(number)

print(x)


user_num = int(input("Please provide a number: "))

for number2 in a:
    if user_num > number2:
        print(number2)


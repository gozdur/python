# program  asks the user for a number and then prints out a list of all the divisors of that number


number = int(input("Provide a number: "))

list = range(1, number + 1)
new_list = []
for divisor in list:
    if number % divisor == 0:
        new_list.append(divisor)

print(new_list)
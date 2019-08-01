# Program asks for age and name and displays a message refering to the neme
# providing info how much years there is left until 100 and what year it will be
# next asks for a diffrent number and displays the message x number of times


from datetime import *

name = input("What is your name?: ")
age = int(input("How old are you?: "))
now = datetime.now()
year = int(now.year)
years_left = 100 - age
the_year = years_left + year

message1 = "Hello " + str(name) + " you have " + str(years_left) + " until you reach 100 years"
message2 = "It will happen in year " + str(the_year)

print(message1)
print(message2)

iteration = int(input("Please provide number of times to display: "))

while iteration > 0:
    iteration = iteration -1
    print(message1)
    print(message2)















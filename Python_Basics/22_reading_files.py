# open function opens a file if in the same directory as python program just type a name otherwise a path and name
# open(xxx, yyy)   xxx == file yyy== mode
# "r" - read mode
# "w" - write mode
# "a" - append information at the end of file not modify existing just add new at the end
# "r+" - read and write

#############################################################################

employees_var = open("employees.txt", "r")         # file is read and stored in variable



print(employees_var.readable()) # function that checks if the file is readable

print(employees_var.readline()) # reads a line and moves cursor to the next line

print(employees_var.read()) # reads full file and prints but because of previous command it starts at second line

employees_var.close() # it will close the file close function used on the variable

print("\n ###############################")

##############################################################################

employees_var = open("employees.txt", "r")         # reopen a file after closure

print(employees_var.readlines()) # .readlines reads it and puts in a list (array)

employees_var.close() # it will close the file close function used on the variable

print("\n ########################################")

################################################################################

employees_var = open("employees.txt", "r")         # reopen a file after closure

for for_var in employees_var.readlines():          # for loop iterates trough employees_var and uses readlines function that makes a list out of data in the variable
    print(for_var)

employees_var.close() # it will close the file close function used on the variable



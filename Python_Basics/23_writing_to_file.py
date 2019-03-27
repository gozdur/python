# open function opens a file if in the same directory as python program just type a name otherwise a path and name
# open(xxx, yyy)   xxx == file yyy== mode
# "r" - read mode
# "w" - write mode
# "a" - append information at the end of file not modify existing just add new at the end
# "r+" - read and write


employees_var = open("employees.txt", "a")
print(employees_var.read())
employees_var.close()
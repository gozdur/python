# open function opens a file if in the same directory as python program just type a name otherwise a path and name
# open(xxx, yyy)   xxx == file yyy== mode
# "r" - read mode
# "w" - write mode   - it will overwrite the file
# "a" - append information at the end of file not modify existing just add new at the end
# "r+" - read and write


employees_var = open("employees.txt", "a")

employees_var.write("Lukasz  - Tower Head")  # it will append to the end of the file where the cursor is and when it runs again it will do the same

employees_var.close()


print("\n ############################################")

employees_var = open("employees.txt", "a")

employees_var.write("\nKelly - HR")  # will append in a new line from the cursor position

employees_var.close()

print("\n ############################################")

employees_var = open("employees1.txt", "w")

employees_var.write("\nKelly - HR")  # will create a new file if doesent exist otherwise overwrite

employees_var.close()





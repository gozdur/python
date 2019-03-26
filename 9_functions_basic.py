# Functions in Python
# Functions are pieces of code that can be called, they perform a certain task
# We can use functions that are embeded in pythor or we can create our own function that we call later

# def is a keyword which defines that its a function say_hi is the name, : - indicates the start of the function
# all lines in a function need to be indented

def say_hi():
    print("Hello !")
say_hi()  # calls the function and executes it
print("bottom")

print("top")


########################################################

# defina a function that requires passing parameters

def say_spadaj(name):
    print("Spadaj " + name)

say_spadaj("Dziadu")  # passes a value to the function
say_spadaj(str(6))    # passes a integer converted to string as a value




# If statements operate on booleans True / False

is_male = True

if is_male:   # defines a condition
    print("You are a male")   # executes if condition is tru (indented stuff print is an example)

print("\n"+"\n")

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are NOT a male nor tall")





if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not is_tall:
    print("You are a mall but not tall")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("you are not a male and not tall")


# Learn Strings and string manipulation

print("Pawel\nGozdur") # \n is a line separator will insert a new line

print("Pawel\"Gozdur") # \ break is used to print something that would execute like " chars

# Strings stored in variables and concatenation of strings

phrase = "string in a variable"
print("\n" + "concatenated " + phrase) # and a line and print variable containing a string

# Usage of functions that can be used on strings example: string.function or variable.function - there are many functions

print(phrase.capitalize()) # takes strings and capitalizes first character
print(phrase.upper()) # takes strings and capitalizes whole string


print(phrase.isupper()) # function will check if characters are uppercase and return boolean True or False
print(phrase.islower()) # function will check if characters are lowercase and return boolean True or False


# Functions can be also used together

print(phrase.upper().isupper()) # converts variable to uppercase and checks if its true that it is uppercase


# len function used to count the string length
# () - inside we specify a value that we give to the function aka parameter
# [] - used to give index of a string

print(len(phrase)) # takes variable phrase that contains a string and counts the number of characters
print(phrase[2]) # grabs third character of a string stored in variable phrase [0] - first char is zero

# index function used to check the index of a character of a string

print(phrase.index("st"))  # index function used to check index of a character or string
print(phrase.index("i"))  # index function used to check index of a character or string

# replace function for strings .replace("value", "value")

print(phrase.replace("variable", "variable_replaced"))


#### Explore more functions later
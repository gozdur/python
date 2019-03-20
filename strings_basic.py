# Learn Strings and string manipulation

#Print with /n line separator

print("Pawel\nGozdur")


#Print with  \<char> is interpreted s "break" it will print something which would be interpreted otherwise

print("Pawel\"Gozdur")
print("\n")

# Strings stored in variables and concatenation of strings

phrase = "string in a variable"
print("\n" + "concatenated " + phrase)

# Usage of functions that can be used on strings example: string.function or variable.function - there are many functions

print(phrase.capitalize()) # takes strings and capitalizes first character
print(phrase.upper()) # takes strings and capitalizes whole string


print(phrase.isupper()) # function will check if characters are uppercase and return boolean True or False
print(phrase.islower()) # function will check if characters are lowercase and return boolean True or False

# Functions can be also used together

print(phrase.upper().isupper()) # converts a string in phrase variable converts it to uppercase and checks if its true that it is uppercase
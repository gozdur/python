# write a translator for imaginary language this will use a for loop in combination with an if statement

#gozdur language
#vowels -> g
#-------------------  vowel = aeiou

#dog -> dgg
#cat -> cgt

def translate_function(value):
    translation = ""
    for letter_var in value:
        if letter_var in "AEIOUaeiou":   # This checks both lower and upper case to make more efficient we could use letter_var.lower() and specify unly aeiou
            if letter_var.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter_var
    return translation


print(translate_function(input("Enter a phrase for translation: ")))

# Fuctions that are used agains lists



lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

print(friends)
print(lucky_numbers)

# Extend function

friends.extend(lucky_numbers)  # adds lits lunky_numbers to the back of the friends list
print(friends)

# Bring back to original

lucky_numbers = [4, 8, 9, 18, 42, 56] # brings back original list content
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"] # brings back original list content

print(friends) # check
print(lucky_numbers) # check

# Append function

friends.append("Olek") # .append will add the new value at the end of the list
print(friends)

# Insert function

friends.insert(1, "Aleksander") # will add a new value on the index position 1 and push other elements to the right
print(friends)

# Remove function

friends.remove("Olek") # removes a value with a name
print(friends)

# Clear function

friends.clear()
print(friends)

# Bring back to original

lucky_numbers = [4, 8, 3, 18, 42, 56] # brings back original list content
friends = ["Kevin", "Jim", "Jack", "Jane", "Oscar","Jim", "Toby"] # brings back original list content

print(friends) # check
print(lucky_numbers) # check

# Pop function

friends.pop() # pops last value from the list
print(friends)

# Index function

print(friends.index("Jane")) # gives the index position of a value specified in the index function

# Count function

print(friends.count("Jim")) # counts how many times a value is present in the list

# Sort Function

friends.sort() # strings are sorted in alphabetical order
lucky_numbers.sort() # numbers are sorted lowest to highest

print(friends)
print(lucky_numbers)

# Reverse the order

friends.reverse() # reverses the order of the list but does not sort
lucky_numbers.reverse() # reverses the order of the list but does not sort

print(friends)
print(lucky_numbers)

# Copy function

friends2 = friends.copy() # creates a new varialble with a copied frinds list
print(friends2)





















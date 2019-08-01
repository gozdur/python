

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("########## Solution 2 ###############")


empty_list = []

for i in a:
    if i in b:
        empty_list.append(i)

print(empty_list)
print("\n")
print("########## Solution 2 ###############")

c = list(set(a)&set(b))

print(c)


print("########## with random ###############")



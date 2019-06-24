# This code writes own function that can be reused later or in other programs

#print(2**3)    # This is actually using a built in function in Python


def raise_to_power(base_num, pow_num):
    result = 1
    for kupa in range(pow_num):       # range iterate range(x) number of times
        result = result * base_num
        print(kupa)
    return result

print(raise_to_power(2, 4))




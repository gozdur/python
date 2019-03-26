
number_grid = [       # this is a 2D list with 4 rows and 3 columns
    [1, 2, 2],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[3][0])  # prints out a column 1 and row 1 of the 2d list,we can provide any coordinate

print("\n")

# NESTED FOR LOOP


for var in number_grid:
    print(var)



for row in number_grid:
    for col in row:
        print(col)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for i in matrix: # for on items
    print(i)
    for j in i:
        print(j)

print("****************")

for i in range(len(matrix)): # for on indexes
    print(matrix[i])
    row = matrix[i]
    for j in row:
        print(j)
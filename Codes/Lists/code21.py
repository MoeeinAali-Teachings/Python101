matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    2
]
print(matrix1)

matrix2 = matrix1.copy() # فقط در سطح ۱ کپی انجام میده!

matrix2[0][0] = "moeein"
matrix2[3] = 5

print(matrix1)
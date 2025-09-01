# 3! = 1 * 2 * 3 
# 1! = 1
# 0! = 1
# 2! = 1 * 2

# faactorial(n) = n * factorial(n-1)
# 7! = 7 * 6!
# 6! = 6 * 5!
#....
# 2! = 2 * 1!
# 1! = 1

def factorial(n):
    print("start:",n)
    if n == 1:
        return 1
    
    return factorial(n-1) * n

print(factorial(6))


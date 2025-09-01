# 1 1 2 3 5 8 13 ...

def fibo(n):
    if n == 1 or n == 2:
        return 1   
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(2))
print(fibo(6))
print(fibo(7))
print(fibo(10))
print(fibo(20))


print("********************")
# F(n) = 3*F(n-1) + 2*F(n-2)
# F(0) = 1
# F(1) = 2

def custom_function(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 3*custom_function(n-1) + 2*custom_function(n-2)

print(custom_function(10)) 
from math import gcd , lcm

def gcd_and_lcm(a,b):
    print("starting...")
    return gcd(a,b) , lcm(a,b)

result1 , result2 = gcd_and_lcm(10,17)

print(result1)
print(result2)
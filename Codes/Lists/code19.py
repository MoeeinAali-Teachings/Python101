list1 = [1,2,3]
print(list1)

list3 = list1.copy() # روش ۱
list3 = list(list1) # روش ۲
list3 = list1[0:] # روش ۳

print(list3)

list3[0] = "moeein"
list1[2] = "saeed"

print(list1)
print(list3)

# Object in RAM
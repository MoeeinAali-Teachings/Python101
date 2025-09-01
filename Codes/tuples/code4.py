fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


print("****************")


names = ("moeein" , "saeed" , "amir" , "reza" , "amir")

name1 , name2 , *anotherNames = names

anotherNames = tuple(anotherNames)

print(name1)
print(name2)
print(anotherNames)
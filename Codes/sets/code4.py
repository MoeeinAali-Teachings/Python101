thisset = {"apple", "banana", "cherry"}

print(thisset)

try:
    thisset.remove("moeein")
except:
    print("error!")
    
thisset.discard("saeed")


print(thisset) 
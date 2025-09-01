def my_function(name,family):
  print("Hello", name , family)

my_function("moeein" , "aali")
# my_function("mamad") # error 

def my_function2(*args):
    print(args[2])

my_function2("moeein" , 2 ,3 , True , 99)
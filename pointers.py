num1 = 11 # We a pointing num1 to be equal to 11

num2 = num1 

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# N.B: integers are immutable can't be changed



dict1 = {
         'value': 11
       }

dict2 = dict1

print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# N.B: Dictionaries are mutable and can be changed


# Why is it important?
# Nodes of LinkedList operates like dictionaries

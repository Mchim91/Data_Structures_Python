# Assign the value 11 to the variable 'num1'.
num1 = 11 # We a pointing num1 to be equal to 11

# Assign the value of 'num1' to the variable 'num2'.
num2 = num1 

# Print the values of 'num1' and 'num2' before 'num2' is updated.
print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Print the memory addresses (IDs) of 'num1' and 'num2'.
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# Update the value of 'num2' to 22.
num2 = 22

# Print the values of 'num1' and 'num2' after 'num2' is updated.
print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Print the memory addresses (IDs) of 'num1' and 'num2'.
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# N.B: Integers are immutable, which means their values cannot be changed in place.

# Create a dictionary 'dict1' with a key 'value' and a value of 11.
dict1 = {'value': 11}

# Assign the dictionary 'dict1' to 'dict2'.
dict2 = dict1

# Print the values of 'dict1' and 'dict2' before the 'value' is updated.
print("Before value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Print the memory addresses (IDs) of 'dict1' and 'dict2'.
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# Update the 'value' in 'dict2' to 22.
dict2['value'] = 22

# Print the values of 'dict1' and 'dict2' after the 'value' is updated.
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Print the memory addresses (IDs) of 'dict1' and 'dict2'.
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# N.B: Dictionaries are mutable, which means their contents can be changed in place.

# The comments in the code explain the concepts of mutability and immutability and how they apply to integers and dictionaries.

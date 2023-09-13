############### BigO #####################
# N.B: For BigO we consider the worst case scenerio
#                       O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# BigO drop constants    O(2n)
def print_items(n):
    for i in range(n):
        print(i) 

    for j in range(n):
        print(j)

print_items(10)


# BigO                   O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)

# BigO                   O(n^2)               
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

print_items(10)

# N.B: O(n^2) is less effecient than O(n)


# BigO drop non-dominants    O(n^2) + O(n) = O(n^2 + n)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)


# BigO                       0(1) Constant time as it increases the number of operations becomes constant
# N.B: It's the most effecient BigO
def add_items(n):
    return n + n


############### BigO O(log n) #####################
# It's very effecient but not more than 0(1)

# BigO(nlog n): It's the most effecient sorting algorithm


# Big O Different terms for inputs
# O(a) + O(b) = O(a + b)
def print_items(a, b):
    for i in range(a):
        print(i) 

    for j in range(b):
        print(j)

# O(a) * O(b) = O(a * b)
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


# Big O Of Lists
# It's a built in data structure
# It's very common


# O(1) - Illustration
my_list = [11,  3, 23, 7] 
# If you want to add or number 17 to the list 
my_list.append(17)
print(my_list)

# If you want to remove number 17 from the list
my_list.pop()
print(my_list)
# N/B: There's no re-indexing occuring in the list


# O(n) - Illustration
my_list2 = [11, 3, 23, 7]
my_list2.pop(0) # This line removes value 11 from the list because it's in index 0 of the index to be popped
print(my_list2)
# N/B: There's re-indexing occuring in the list because when the value is popped out the index now starts from 1 - 3

# To insert the value back into the list we do
my_list2.insert(0, 11)
print(my_list2)

# Terminologies summary
# O(n^2) - Loop within a loop 
# O(n) - It's proprtional it would always be a straight line
# O(log n) - It's Divide and Conquer
# O(1) - Constant time  

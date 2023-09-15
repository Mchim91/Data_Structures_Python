# Dictionaries are built-in hast table
# It consits of a key and a hash function and returns an adress

# Characteristics of hash
# 1.) It's one way only
# 2.) It's deterministic (We know the adress)

# Collision - it's putting a key value pair in the same address table of another key value pair
# Separate Chaining:
# Separate chaining is a collision resolution technique in hash tables.
# In separate chaining, each bucket (or slot) in the hash table contains a linked list or another data structure that can hold multiple key-value pairs.
# When a collision occurs (i.e., two keys hash to the same bucket), the new key-value pair is simply added to the linked list at that bucket.
# This allows multiple key-value pairs to coexist in the same bucket without overwriting each other.
# Linear Probing:

# Linear probing (open addressing) is another collision resolution technique in hash tables.
# In linear probing, when a collision occurs, the algorithm looks for the next available (empty) slot in the hash table by incrementing the index.
# If the next slot is also occupied, it continues to search for the next empty slot in a linear fashion (hence the name "linear probing").
# This process continues until an empty slot is found, and the key-value pair is placed in that slot.
# Retrieving values involves a similar linear search until the key is found or an empty slot is encountered.

# Building the constructor
# N.B You should always have a prime number for addressing
class HashTable:
    # Initialize a hash table with a given size, defaulting to 7.
    def __init__(self, size = 7):
        self.data_map = [None] * size


# Creating a hash method to calculate the index for a given key.
    # O(1)
    def __hash(self, key):
        my_hash = 0
        # Iterate through each character in the key.
        for letter in key:
            # Update the hash using the ASCII value of the character and a constant multiplier (23).
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  


    # Method to print the hash table.
    # O(1)
    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    

    # Method to set an item in the hash table.
    def set_item(self, key, value):
        # Calculate the index for the key using the hash method.
        index = self.__hash(key)
        # Check if the slot is empty (None).
        if self.data_map[index] == None:
            # If empty, initialize it as an empty list.
            self.data_map[index] = []
        # Append the key-value pair to the list at the calculated index.  
        self.data_map[index].append([key,value])

    # Method to get the value associated with a given key.
    def get_item(self, key):
        # Calculate the index for the key using the hash method.
        index = self.__hash(key)
        # Check if the slot is not empty.
        if self.data_map[index] is not None:
            # Iterate through the list at the calculated index.
            for i in range(len(self.data_map[index])):
                # If the key matches, return the associated value.
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # If the key is not found, return None.
        return None
    

    # Method to retrieve all keys from the hash table.
    def keys(self):
        all_keys = []
        # Iterate through each slot in the hash table
        for i in range(len(self.data_map)):
            # Check if the slot is not empty.
            if self.data_map[i] is not None:
                # Iterate through the list at the slot.
                for j in range(len(self.data_map[i])):
                    # Append the key to the list of all keys.
                    all_keys.append(self.data_map[i][j] [0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.print_table()


# Method to set_item
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()


# Method get set_item
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))


# Method to get all keys
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())


# Interview Question
# You're placed with 2 list how do you check if they have an item in common

# 1st approach (naive approach)
# O(n^2)
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]
print(item_in_common(list1, list2))


# 2nd approach ()
# O(n)
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]
print(item_in_common(list1, list2))

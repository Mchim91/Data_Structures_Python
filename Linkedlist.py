# It doesn't have an index
# It's a continues place in memory
# All the nodes are going to be spread all over the place
# We have a variable called head and it points to the first node in the list
# We have a variable called tail that points to the last node in the last
# Each node points to the next and to the next


# Linkedlist BigO
# Adding an item to the TAIL is O(1)
# Removing an item from the TAIL is O(n)
# Adding an item to the HEAD is O(1)
# Removing an item from the HEAD is O(1)
# Adding an item to somewhere in the list is O(n)
# Removing an item to somewhere in the list is O(n)
# Look up in a Linked List


# Comparing LinkedLists to Lists
#                   Linked Lists         Lists
# Append            O(1)                 O(1)
# Pop               O(n)                 O(1)
# Prepend           O(1)                 O(n)
# Pop First         O(1)                 O(n)
# Insert            O(n)                 O(n)
# Remove            O(n)                 O(n)
# Lookup by index   O(n)                 O(1)
# lookup by Value   O(n)                 O(n)

# Node - it's a dictionary 

head = {
    "value": 11,
    "next": {
             "value": 3,
             "next": {
                      "value": 23,
                      "next" : {
                                "value": 7,
                                "next": {
                                         "value": 4,
                                         "next": None  #### Tail
                                }
                      }
             }
    }
}

print(head['next']['next']['value'])

# This will only run with a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# How to use the example above for a Linkedlist
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # Print the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    # Method to append to the end of a Linked List
    # Big O:
    # O( 1 )
    # Constant Time
    # No matter how large the linked list is, the number of operations taken to execute append remains constant
    # Constant time is another name for O( 1 )
    def append(self, value):
        # Create a node with the given value:
        new_node = Node(value)
        # Check if the linked list is empty
        if self.head is None: # or you can write it like this ###### if self.length == 0;
            # If the Linkedlist is empty, set the head and tail to point at new_node:
            self.head = new_node
            self.tail = new_node
        # When there's an item at the end of the linked list 
        else:
            # If the head is not None (which means the LL has at least one node), update the next attribute of the node tail is pointing to, to point to new_node:
            self.tail.next = new_node
            # Set tail to point to new_node:
            self.tail = new_node
        # Increment the length of the linked list by 1:
        self.length += 1
        return True
    
    
    # Popping an item off from the Linked list
    # Big O:
    # O( n )
    # n is the number of nodes in the linked list
    # When we say that the time complexity of a linked list operation is O(n), we mean that the execution time of the operation grows linearly with the size of the linked list. In other words, as the number of elements in the linked list increases, the time taken to perform the operation increases at the same rate.
    # An algorithm with a single loop that iterates through all n items in the worst case has a time complexity of O(n)
    # This is what lets us know this is O(n):
    def pop(self):
        # Check if the Linkedlist is equal to None
        if self.length == 0:
            return None
        # set a temp variable to the head of the Linkedlist
        temp = self.head
        # set a prev (previous) variable to the head of the Linkedlist also
        pre = self.head
        # As long the next item of the temp variable is not equals to None
        while (temp.next) is not None:
            # Assign the prev to temp because both of them are assigned to the Head of the Linkedlist
            pre = temp
            # Point the temp variable to the temp.next
            temp = temp.next
        # Assign the tail variable to pre
        self.tail = pre
        # Decrement the Linkedlist
        self.length -= 1
        # if the Linkedlist is equals to None
        if self.length == 0:
            # Assign the head & tail to None
            self.head = None
            self.tail = None
        # Return the temp & you can also return the value by using return temp.value
        return temp
    

    # Prepend - adding an item to the beginning of a Linked list
    # It's a O(1) algorithm 
    def predend(self, value):
        # Create a new node with given values
        new_node = Node(value)
        # Check if the length of the Linkedlist is empty
        if self.length == 0:
            # If it's not empty assign head & tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Assign the next value of the new not to the head
            new_node.next = self.head
            # Assign the head to the new node
            self.head = new_node  
        # Increment the Linkedlist 
        self.length += 1
        # Return True
        return True
    

    # Pop the first item out of a list
    # It's a O(1)
    def pop_first(self):
        # Check if the list is empty
        if self.length == 0:
            # If it's empty return None
            return None
        # Assign temp variable to the head
        temp = self.head
        # Assign head variable to the next head item in the Linkedlist
        self.head = self.head.next
        # Assign the next temp variable to None
        temp.next = None
        # Decrement the length of the linkedlist
        self.length -= 1
        # check if the length of the linkedlist is 
        if self.length == 0:
            self.tail = None
        # Return the temp variable
        return temp
    

    # Get
    # It's a O(n) operation
    def get(self, index):
        # Check if the index is less than 0 or the index is greater than of equal to the Linkedlist
        if index < 0 or index >= self.length:
            return None
        # Assign the temp variable to the head
        temp = self.head
        # The for loop makes us know that it's O(n)
        # Keep iterating through the linkedlist and check the indexes
        for _ in range(index):
            # Assign the temp variable to the next item in the temp
            temp = temp.next
        # Return the temp
        return temp
    

    # Set 
    # It's O(n) operation
    def set_value(self, index, value):
        # Using the get method in the set method and assign it to the temp variable
        temp = self.get(index)
        # The loop is an evidence that it's O(n) operation
        # Check if the temp is not None
        if temp is not None:
            # Assign a value to the temp variable and then assign it to a value
            temp.value = value
            # Return True afterwards
            return True
        # Retrun False afterwards
        return False
    

    # insert a node into the Linked list
    # It's O(n) operation
    def insert(self, index, value):
        # Check if the index is less than 0 or index is greater than or equal to the length of the of the Linkedlist
        if index < 0 or index >= self.length:
            return False
        # Check if the index is equal to 0
        if index == 0:
            # Return the attached value to the begining of the Linkedlist using the prepend method which we handled earlier
            return self.predend(value)
        # Check if the index is equal to the length of the Linkedlist
        if index == self.length:
            # Return the attached value the end of the Linkedlist using the append method which was handled earlier
            return self.append(value)
        # Assign a new node variable to the Node of type value
        new_node = Node(value)
        # Assign a temp variable to get method index and decrement the value of the index by 1
        temp = self.get(index - 1)
        # Create the next new node variable and pass to the temp next
        new_node.next = temp.next
        # Then equate the temp next variable to the new node
        temp.next = new_node
        # Increment the length of the Linkedlist
        self.length += 1
        # Return True
        return True
    

    # remove an item from a particular Linkedlist
    # It's O(n) operation
    def remove(self, index):
        # Check if the index is less than 0 or index is greater than or equal to the length of the of the Linkedlist 
        if index < 0 or index >= self.length:
            return None
        # Check if the index is equal to zero
        if index == 0:
            # Return pop_first method which was created earlier used to remove the first item from the Linkedlist
            return self.pop_first()
        # Check if the index is equal to the decrement of the lenght of the Linkedlist
        if index == self.length - 1:
            # Return pop method which was created earlier to remove and item from a list
            return self.pop()
        # Assign a previous variable to a get method that was created earlier which passes the decrement of the index
        prev = self.get(index - 1)
        # temp = self.get(index - 1) This line of code would still work but it's ineffecient because
        # the get method is O(n) but there is a O(1) way of assigning the temp variable which is what is done below  
        temp = prev.next
        prev.next = temp.next
        # To break the node
        temp.next = None
        self.length -= 1
        return temp
    

    # reverse an item from a Linkedlist
    # N.B: It's a very common interview question
    # Steps
    # 1.) Assign a temp to the head
    # 2.) Assign the head to a tail
    # 3.) Assign the tail to temp
    # 4.) Assign a variable on the right of temp called (after) and one at the left of temp called (before) which would point to None
    # 5.) The three variables would iterate through the linkedlist as we are reversing everthing
    # 6.) We have a for loop that goes through the lenght of the Linkedlist
    # 7.) We now have the after to be equals to the temp.next & the temp.next would be equals to the before variable
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            # 8) This makes sure that the Linkedlist doesn't break because of the gap that's created
            before = temp
            temp = after

        
# N.B : The first return in the insert and the remove return both False & None respectively because
#       if we are successful in the insert method we would return true and if not we would return false
#       if we are successful in the remove method we would return a node and if not we would return None because it's an opposite for Node
            

my_linked_list = LinkedList(2)

my_linked_list.append(3)

my_linked_list.predend(1)

my_linked_list.pop_first()


# (2) Items - Return 2 Node
print(my_linked_list.pop())
# (1) Item - Return 1 Node
print(my_linked_list.pop())
# (0) Itmes - Return None
print(my_linked_list.pop())


# (2) Items - Return 2 Node
print(my_linked_list.pop_first())
# (1) Item - Return 1 Node
print(my_linked_list.pop_first())
# (0) Itmes - Return None
print(my_linked_list.pop_first())

my_linked_list.print_list()


# Illustration for the get method
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))


# Illustration for the set method
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1, 4)

print(my_linked_list.print_list())


# Illustration for insert method
my_linked_list = LinkedList(0)
my_linked_list.append(2)

my_linked_list.insert(1, 1)

my_linked_list.print_list()


# Illustration for the remove method
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print(my_linked_list.remove(2), '\n')

my_linked_list.print_list()




############################### Leetcode Exercises ################################

# 1.) Find Middle Node
# Instructions: Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
# Answer
def find_middle_node(self):
    # Initialize two pointers to the head of the list
    slow = self.head
    fast = self.head

    # Traverse the list with the fast pointer moving twice
    # as fast as the slow pointer
    while fast is not None and fast.next is not None:
        slow = slow.next # Move slow pointer one step
        fast = fast.next.next # Move fast pointer two steps

    # When the fast pointer reaches the end, the slow
    # pointer will be at the middle node
    return slow


# 2.) Has Loop
# Instructions:
# LL: Has Loop (⚡Interview Question)
# Write a method called has_loop that is part of the linked list class.
# The method should be able to detect if there is a cycle or loop present in the linked list.
# The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
# The method should follow these guidelines:

# Create two pointers, slow and fast, both initially pointing to the head of the linked list.
# Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
# If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
# If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.
# Answer
def has_loop(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    else:
        return False
    

# 3.) Remove Duplicates
# Instructions:
# LL: Remove Duplicates (⚡Interview Question)
# You are given a singly linked list that contains integer values, where some of these values may be duplicated.
# Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
# Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
# You can implement the remove_duplicates() method in two different ways:

# Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.
# Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. You are not allowed to use any additional data structures for this implementation.
# Here is the method signature you need to implement:
# def remove_duplicates(self):
# Example:
# Input:
# LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
# Output:
# LinkedList: 1 -> 2 -> 3 -> 4 -> 5
# Answer
def remove_duplicates(self):
    values = set()
    previous = None
    current = self.head
    while current:
        if current.value in values:
            previous.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            previous = current
        current = current.next

# Same solution without using set function
def remove_duplicates(self):
    current = self.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
                self.length -= 1
            else:
                runner = runner.next
        current = current.next



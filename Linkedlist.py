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
        temp = self.head  # Initialize a temporary pointer to the head of the linked list.

        while temp is not None:
            print(temp.value) # Print the value of the current node.
            temp = temp.next  # Move the temporary pointer to the next node.


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
        if self.head is None: # Check if the head is None, indicating an empty linked list.
            # If the linked list is empty, set both the head and tail to point to the new_node:
            self.head = new_node
            self.tail = new_node
        # When there's at least one item in the linked list:
        else:
            # Update the next attribute of the node tail is pointing to, to point to new_node:
            self.tail.next = new_node
            # Update the tail to point to new_node, making it the new tail of the linked list:
            self.tail = new_node

        # Increment the length of the linked list by 1 to keep track of the number of elements:
        self.length += 1

        # Return True to indicate successful insertion of the new node:
        return True
    
    
    # Popping an item off from the Linked list
    # Big O:
    # O( n )
    # n is the number of nodes in the linked list
    # When we say that the time complexity of a linked list operation is O(n), we mean that the execution time of the operation grows linearly with the size of the linked list. In other words, as the number of elements in the linked list increases, the time taken to perform the operation increases at the same rate.
    # An algorithm with a single loop that iterates through all n items in the worst case has a time complexity of O(n)
    # This is what lets us know this is O(n):
    def pop(self):
        # Check if the linked list is empty (has a length of 0):
        if self.length == 0:
            return None # If it's empty, there's nothing to pop, so return None.
        
        # Initialize a temporary variable 'temp' to the head of the linked list:
        temp = self.head

        # Initialize a previous variable 'pre' to the head of the linked list as well:
        pre = self.head

        # Traverse the linked list until 'temp' reaches the last node (where temp.next is None):
        while (temp.next) is not None:
            # Update 'pre' to be the same as 'temp' because both are initially set to the head:
            pre = temp

            # Update the tail of the linked list to be the previous node 'pre':
            temp = temp.next

        # Update the tail of the linked list to be the previous node 'pre':
        self.tail = pre

        # Decrement the length of the linked list by 1 to reflect the removal of the last node:
        self.length -= 1

        # If the linked list is now empty:
        if self.length == 0:
            # Set both the head and tail to None to indicate an empty list:
            self.head = None
            self.tail = None

        # Return the node that was removed (the last node, 'temp'):
        return temp
    

    # Prepend - adding an item to the beginning of a Linked list
    # It's a O(1) algorithm 
    def predend(self, value):
         # Create a new node with the given value:
        new_node = Node(value)
        
        # Check if the linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, assign both the head and tail to the new node:
            self.head = new_node
            self.tail = new_node
        else:
            # If the linked list is not empty:
            # Assign the 'next' attribute of the new node to point to the current head:
            new_node.next = self.head
            # Update the head to be the new node, effectively making it the new head:
            self.head = new_node  

        # Increment the length of the linked list by 1 to reflect the addition of the new node: 
        self.length += 1

        # Return True to indicate successful insertion at the beginning:
        return True
    

    # Pop the first item out of a list
    # It's a O(1)
    def pop_first(self):
        # Check if the linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, return None because there's nothing to pop.
            return None
        
        # Assign a temporary variable 'temp' to the current head:
        temp = self.head

        # Update the head to point to the next head item in the linked list,
        # effectively removing the current head from the list:
        self.head = self.head.next

        # Set the 'next' attribute of 'temp' to None to remove its link to the rest of the list:
        temp.next = None

        # Decrement the length of the linked list by 1 to reflect the removal of the first node:
        self.length -= 1

        # Check if the linked list is now empty: 
        if self.length == 0:
            # If it's empty, set the tail to None to indicate an empty list.
            self.tail = None

        # Return the 'temp' variable, which contains the removed node.
        return temp
    

    # Get
    # It's a O(n) operation
    def get(self, index):
        # Check if the index is less than 0 or greater than or equal to the length of the linked list:
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None.
            return None
        
        # Assign a temporary variable 'temp' to the head of the linked list:
        temp = self.head

        # Iterate through the linked list to find the node at the specified index.
        # The loop makes it clear that the time complexity is O(n), where 'n' is the number of nodes in the list.
        for _ in range(index):
            # Move 'temp' to the next node in the linked list.
            temp = temp.next

        # Return the 'temp' variable, which now points to the node at the specified index.
        return temp
    

    # Set 
    # It's O(n) operation
    def set_value(self, index, value):
        # Use the 'get' method to retrieve the node at the specified index and assign it to the 'temp' variable.
        temp = self.get(index)

        # Check if the 'temp' variable is not None (i.e., a valid node was found).
        if temp is not None:
            # Set the 'value' attribute of the 'temp' node to the provided 'value'.
            temp.value = value

            # Return True to indicate that the value was successfully updated.
            return True
        
        # If 'temp' is None, it means the index was out of bounds or the linked list is empty.
        # Return False to indicate that the value was not updated.
        return False
    

    # insert a node into the Linked list
    # It's O(n) operation
    def insert(self, index, value):
        # Check if the index is less than 0 or greater than or equal to the length of the linked list:
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return False because insertion is not possible.
            return False
        
        # Check if the index is equal to 0, indicating insertion at the beginning of the list:
        if index == 0:
            # Use the 'prepend' method to insert the value at the beginning and return the result.
            return self.predend(value)
        
        # Check if the index is equal to the length of the linked list, indicating insertion at the end:
        if index == self.length:
            # Use the 'append' method to insert the value at the end and return the result.
            return self.append(value)
        
        # Create a new node with the provided 'value':
        new_node = Node(value)

        # Use the 'get' method to retrieve the node at 'index - 1' and assign it to 'temp':
        temp = self.get(index - 1)

        # Make the new node's 'next' attribute point to the same node that 'temp' is pointing to:
        new_node.next = temp.next

        # Update the 'next' attribute of 'temp' to point to the new node, effectively inserting it into the list:
        temp.next = new_node

        # Increment the length of the linked list to reflect the addition of the new node:
        self.length += 1

        # Return True to indicate successful insertion.
        return True
    

    # remove an item from a particular Linkedlist
    # It's O(n) operation
    def remove(self, index):
        # Check if the index is less than 0 or greater than or equal to the length of the linked list:
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None because removal is not possible.
            return None
        
        # Check if the index is equal to 0, which indicates removal of the first item in the list:
        if index == 0:
            # Use the 'pop_first' method to remove and return the first item from the linked list.
            return self.pop_first()
        
        # Check if the index is equal to the length of the linked list minus 1, indicating removal of the last item:
        if index == self.length - 1:
            # Use the 'pop' method to remove and return the last item from the linked list.
            return self.pop()
            
        # Assign 'temp' directly to the 'next' attribute of 'prev', making it O(1) instead of calling 'get' again:
        prev = self.get(index - 1) 

        # Assign 'temp' directly to the 'next' attribute of 'prev', making it O(1) instead of calling 'get' again:
        temp = prev.next

        # Update the 'next' attribute of 'prev' to point to the node following 'temp', effectively removing 'temp' from the list:
        prev.next = temp.next

        # Break the link by setting the 'next' attribute of 'temp' to None:
        temp.next = None

        # Decrement the length of the linked list to reflect the removal of the node:
        self.length -= 1

         # Return the removed node, which is 'temp':
        return temp
    

    # reverse an item from a Linkedlist
    # N.B: It's a very common interview question
    def reverse(self):
        # Swap the head and tail pointers to reverse the direction of the linked list.
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # Initialize 'after' to the 'next' node of 'temp' and 'before' to None.
        after = temp.next
        before = None

        # Iterate through the linked list to reverse the order of nodes.
        for _ in range(self.length):
            # Store the 'next' node of 'temp' in 'after'.
            after = temp.next

            # Reverse the direction by setting the 'next' attribute of 'temp' to 'before'.
            temp.next = before

            # Move 'before' and 'temp' pointers one step forward in the linked list.
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

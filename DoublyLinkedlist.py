# Create a Node class and initialize 
# N.B: DLL(Doubly Linked List)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # Print the list
    def print_list(self):
        temp = self.head # Initialize a temporary pointer to the head of the linked list.

        while temp is not None: 
            print(temp.value) # Print the value of the current node.
            temp = temp.next # Move the temporary pointer to the next node.

    
    def append(self, value):
        # Create a new node with the given value:
        new_node = Node(value)

        # Check if the linked list is empty (head is None):
        if self.head is None:
            # If it's empty, set both the head and tail to point to the new node:
            self.head = new_node
            self.tail = new_node
        else:
            # If the linked list is not empty:
            # Attach the new node to the next attribute of the current tail node:
            self.tail.next = new_node
            # Assign the current tail node as the previous node of the new node:
            new_node.prev = self.tail
            # Update the tail to point to the new node, making it the new tail:
            self.tail = new_node

        # Increment the length of the doubly linked list by 1 to reflect the addition of the new node:
        self.length += 1

        # Return True to indicate successful appending of the new node:
        return True
    

    # Code A
    def pop(self):
        # Check if the doubly linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, return None because there's nothing to pop.
            return None
        
        # Introduce a variable 'temp' pointing to the current tail node:
        temp = self.tail

        # Move the tail pointer to the previous node, effectively removing the current tail:
        self.tail = self.tail.prev 

        # Break the connection between the previous tail node and the removed node: 
        self.tail.next = None
        temp.prev = None

        # Decrement the length of the doubly linked list by 1 to reflect the removal of the node:
        self.length -= 1

        # If the doubly linked list is now empty:
        if self.length == 0:
            # Assign both the head and tail to None to indicate an empty list:
            self.head = None
            self.tail = None

        # Return the removed node, which is 'temp':  
        return temp
    # OR
    # Code B
    def pop(self):
        # Check if the doubly linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, return None because there's nothing to pop.
            return None
        
        # Introduce a variable 'temp' pointing to the current tail node:
        temp = self.tail

        # Check if the length of the doubly linked list is 1 (only one node in the list):
        if self.length == 1:
            # In this case, there's only one node in the list, so set both the head and tail to None,
            # effectively making the list empty.
            self.head = None
            self.tail = None
        else:
            # If there's more than one node in the list:
            # Move the tail pointer to the previous node, effectively removing the current tail node:
            self.tail = self.tail.prev
            # Break the connection between the new tail node and the removed node by setting the 'next' attribute to None:
            self.tail.next = None
            # Break the connection between the removed node and the new tail node by setting the 'prev' attribute to None:
            temp.prev = None

        # Decrement the length of the doubly linked list by 1 to reflect the removal of the node:
        self.length -= 1

        # Return the removed node, which is 'temp':
        return temp
    
    # Which is better? Code A or Code B


    def prepend(self, value):
        # Create a new node with the given value:
        new_node = Node(value)

        # Check if the doubly linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, set both the head and tail to point to the new node,
            # because the new node becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
        else:
            # If there are already nodes in the list: 
            # Set the 'next' pointer of the new node to point to the current head node.
            new_node.next = self.head
            # Set the 'prev' pointer of the current head node to point back to the new node.
            self.head.prev = new_node
            # Update the head to point to the new node, making it the new head node.
            self.head = new_node

        # Increment the length of the doubly linked list by 1 to reflect the addition of the new node:   
        self.length += 1

        # Return True to indicate successful prepending of the new node:
        return True
    

    def pop_first(self):
        # Check if the doubly linked list is empty (has a length of 0):
        if self.length == 0:
            # If it's empty, return None because there's nothing to pop.
            return None
        
        # Introduce a temporary variable 'temp' to hold the current head node:
        temp = self.head

        # Check if the length of the doubly linked list is 1 (only one node in the list):
        if self.length == 1:
           # In this case, there's only one node in the list, so set both the head and tail to None,
           # effectively making the list empty.
           self.head = None
           self.tail = None
        else:
            # If there are two or more nodes in the list:
            # Move the head pointer to the next node, effectively removing the current head node:
            self.head = self.head.next
            # Set the 'prev' attribute of the new head node to None, breaking the connection to the removed node.
            self.head.prev = None
            # Break the connection between 'temp' and the new head node by setting the 'next' attribute of 'temp' to None.
            temp.next = None

        # Decrement the length of the doubly linked list by 1 to reflect the removal of the node: 
        self.length -= 1

        # Return the removed node, which is 'temp':
        return temp

    
    def get(self, index):
        # Check if the provided index is out of bounds (less than 0 or greater than or equal to the length of the linked list):
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None because the requested node does not exist.
            return None
        
        # Initialize a temporary variable 'temp' to the head node.
        temp = self.head

        # Iterate through the linked list 'index' times to reach the desired node:
        for _ in range(index):
            # Move 'temp' to the next node in the list.
            temp = temp.next

        # Return the node at the specified index, which is now stored in 'temp': 
        return temp
    
    
    # Optimized code for the get method
    # In this part we consider accessing indexes using both from the head or tail
    def get(self, index):
        # Check if the provided index is out of bounds (less than 0 or greater than or equal to the length of the linked list):
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None because the requested node does not exist.
            return None
        
        # Initialize a temporary variable 'temp' to the head node.
        temp = self.head

        # Check if the requested index is in the first half of the linked list:
        if index < self.length / 2:
            # If the index is in the first half, iterate forward through the linked list to reach the desired node.
            for _ in range(index):
                temp = temp.next
        else:
            # If the index is in the last half of the linked list:
            # Set 'temp' to be equal to the tail node (end of the doubly linked list).
            temp = self.tail

            # Iterate backward through the linked list to reach the desired node.
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        # Return the node at the specified index, which is now stored in 'temp':
        return temp
    

    def set_value(self, index, value):
        # Use the 'get' method to retrieve the node at the specified index and store it in 'temp':
        temp = self.get(index)

        # Check if 'temp' is not None, meaning the requested index is valid and the node exists:
        if temp:
            # Set the 'value' attribute of the node at the specified index to the new 'value':
            temp.value = value

            # Return True to indicate that the value was successfully updated:
            return True
        
        # If 'temp' is None, it means the requested index is out of bounds and the value was not updated:
        return False
    

    def insert(self, index, value):
        # Check if the provided index is out of bounds (less than 0 or greater than or equal to the length of the linked list):
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None because the insertion is not possible.
            return None
        
        # Check if the requested index is 0, which means the new value should be inserted at the front of the list:
        if index == 0:
            return self.prepend(value)
        
        # Check if the requested index is equal to the current length, which means the new value should be inserted at the back of the list:
        if index == self.length:
            return self.append(value)
        
        # If you want to insert into the middle of the doubly linked list, create a new node with the given value:
        new_node = Node(value)

        # Retrieve the node before the desired index and the node after the desired index:
        before = self.get(index - 1)
        after = before.next

        # Update the 'prev' and 'next' pointers to insert the new node between 'before' and 'after':
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        # Increment the length of the doubly linked list by 1 to reflect the insertion of the new node:
        self.length += 1

        # Return True to indicate successful insertion:
        return True
    

    def remove(self, index):
        # Check if the provided index is out of bounds (less than 0 or greater than or equal to the length of the linked list):
        if index < 0 or index >= self.length:
            # If the index is out of bounds, return None because the removal is not possible.
            return None
        
        # Check if the requested index is 0, which means the first item should be removed:
        if index == 0:
            return self.pop_first()
        
        # Check if the requested index is equal to the last index, which means the last item should be removed:
        if index == self.length - 1:
            return self.pop() 
        

        # Check if the requested index is equal to the last index, which means the last item should be removed:
        temp = self.get(index)

        # Remove the node by updating the 'prev' and 'next' pointers to bypass 'temp':
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        # Clear the 'next' and 'prev' pointers of 'temp' to disconnect it from the list:
        temp.next = None
        temp.prev = None

        # Decrement the length of the doubly linked list by 1 to reflect the removal of the node:
        self.length -= 1

        # Return the removed node:
        return temp


# Illustration for printing a list
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()


# Illustration for append method
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()


# Illustration for pop method
# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop())
# (1) Item - Returns 1 Node
print(my_doubly_linked_list.pop())
# (0) Items - Returns None
print(my_doubly_linked_list.pop())


# Illustration for prepend method
my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

my_doubly_linked_list.prepend(1)

my_doubly_linked_list.print_list()


# Illustration for pop_first method
my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first())
# (1) Item - Returns 1 Node
print(my_doubly_linked_list.pop_first())
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())


# Illustration for get method
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print(my_doubly_linked_list.get(1))
print(my_doubly_linked_list.get(2))


# Illustration for set method
my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print(my_doubly_linked_list.set_value(1, 4))

my_doubly_linked_list.print_list()


# Illustration for insert method
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

my_doubly_linked_list.insert(1, 2)

my_doubly_linked_list.print_list()


# Illustration for remove method
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

print(my_doubly_linked_list.remove(1), '\n')

my_doubly_linked_list.print_list()




############################### Leetcode Exercises ################################

# 1.) DLL SWAP FIRST AND LAST
# Instructions:
# DLL: Swap First and Last (⚡Interview Question)
# Swap the values of the first and last node

# Method name:
# swap_first_last

# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.
# Answer
def swap_first_last(self):
    # Check if the list is empty or has only one node
    if self.head is None or self.head == self.tail:
        return 
    self.head.value, self.tail.value = self.tail.value, self.head.value


# 2.) DLL REVERSE
# Instructions:
# DLL: Reverse (⚡Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction. Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.
# Answer
def reverse(self):
    temp = self.head
    while temp is not None:
        # swap the prev and next pointers of the node points to
        temp.prev, temp.next, temp.prev
        # move to the next node
        temp = temp.prev
    # swap the head and tail pointers
    self.head, self.tail = self.tail, self.head


# 3.) DLL PALINDROME CHECKER
# Instructions:
# DLL: Palindrome Checker (⚡Interview Question)
# Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

# For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since the list is a palindrome.

# If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list is not a palindrome.
# Answer
def is_palidrone(self):
    # If the length of the list is 0 or 1, it's always a palidrome
    if self.lenght <= 1:
        return True
    # Create two pointers, one starting from the head and the other from the tail
    forward_node = self.head
    backward_node = self.tail
    # Iterate over half of the list
    for _ in range(self.length // 2):
        # If the values at the tweo ends of the list do not match, the list is not a palidrome
        if forward_node.value != backward_node.value:
            return False
        # Move the teo pointers towards each other
        forward_node = forward_node.next
        backward_node = backward_node.next
    # If all values matches, the list is a palidrome
    return True


# 4.) DLL SWAP NODES IN PAIRS
# Instructions:
# DLL: Swap Nodes in Pairs (⚡Interview Question)
# You are given a doubly linked list.

# Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

# Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

# Example:

# 1-->2-->3-->4--> should become 2-->1-->4-->3-->

# Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

# Note: You must solve the problem without modifying the values in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)
def swap_pairs(self):
    # Create dummy node as a placeholder
    dummy = Node(0)
    # Connect dummy node to head
    dummy.next = self.head
    # set prev as a dummy node
    prev = dummy
    # Iterate through the list while a pair exists
    while self.head and self.head.next:
        # Assign first and second nodes of the pair
        first_node = self.head
        second_node = self.head.next
        # Swap the pair by updating pointers
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        # Update prev pointers for swapped nodes
        second_node.prev = prev
        first_node.prev = second_node
        # Update prev pointer of the next node
        if first_node.next:
            first_node.next.prev = first_node
        # Move head to the next pair
        self.head = first_node.next
        # Update prev to the last node in the pair
        prev = first_node
    # Update the head to the new start
    self.head = dummy.next
 

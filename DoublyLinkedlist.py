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
        # Create a variable named temp and set it to the head of the DLL
        temp = self.head
        # Check is the temp is not None
        while temp is not None:
            # Print the value attached to the temp variable
            print(temp.value)
            # Assign the same temp variable to the next item of the variable
            temp = temp.next

    
    def append(self, value):
        # create a new node and attach it to Node class created previously
        new_node = Node(value)
        # Check if the head node is None and if it's None
        if self.head is None:
            # Attach the head and tail item to a new node
            self.head = new_node
            self.tail = new_node
        else:
            # Attach the next tail item to a new node
            self.tail.next = new_node
            # Assign the previous new node to the tail
            new_node.prev = self.tail
            # Assign the tail to the new node
            self.tail = new_node
        # increment the DLL
        self.length += 1
        # Return True
        return True
    

    # Code A
    def pop(self):
        # When you don't have an item in the DLL
        if self.length == 0:
            return None
        # Introduce a variable pointing to the tail called temp
        temp = self.tail
        # Move tail over
        self.tail = self.tail.prev 
        # Break the connection between the two arrows 
        self.tail.next = None
        temp.prev = None
        # Decrement the list by 1
        self.length -= 1
        # if the Linkedlist is equals to None
        if self.length == 0:
            # Assign the head & tail to None
            self.head = None
            self.tail = None
        return temp
    # OR
    # Code B
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    # Which is better? Code A or Code B


    def prepend(self, value):
        # Create node to be prepended to the list
        new_node = Node(value)
        # Code for when you don't have any item on the DLL
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # When there's a DLL with item inside
        else: 
            # Next pointer on the new node point the same node that header is pointed to
            new_node.next = self.head
            # Pointer from the head pointing back to the previous 
            self.head.prev = new_node
            # Point the head to the new node
            self.head = new_node
        self.length += 1
        return True
    

    def pop_first(self):
        # If you don't have any item in the DLL
        if self.length == 0:
            return None
        # If you have just one item in the DLL
        # Introduce a temp variable
        temp = self.head
        if self.length == 1:
           self.head = None
           self.tail = None
        # If we have two or more items in the DLL
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
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




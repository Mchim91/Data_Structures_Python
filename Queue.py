################################# QUEUE ####################################
# Queue - Think about people standing in a line
# It uses FIFO (First-in, First-out)
# Keywords - Enqueue & Dequeue
# N.B: For something to be a queue we add on one end


# When working with Queue we have two ends and each end can be used to add and remove from the queue
# In order to have a very optimized code we need to avoid using O(n) so 
# We enqueue from the from and dequeue from the back because both end up having O(N) operations
# We are going to call Head & Tail to be First & Last
top = {
    "value": 4,
    "next": None
}

# Builing queue constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating our queue class
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    # print method for queue
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

            
    #  enqueue method
    def enqueue(self, value):
        new_node = Node(value)
        # If there's no item on the list
        if self.first is None:
            self.first = new_node
            self.last = new_node
        # If there are items on the list
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    
    #  dequeue method
    def dequeue(self):
        if self.length == 0:
            return None
        # Assign a variable to the first node to remove one item
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


# Method to print queue
# my_queue = Queue(4)

# my_queue.print_queue()


# Method to enqueue queue
# my_queue = Queue(4)
# my_queue.enqueue(2)

# my_queue.print_queue()


# Method to dequeue queue
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Return 2 Node
print(my_queue.dequeue())
# (1) Item - Return 1 Node
print(my_queue.dequeue())
# (0) Itmes - Return None
print(my_queue.dequeue())

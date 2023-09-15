############################# STACK ########################################################
# Stack - Think about sets tennis balls inside it's pack when you first buy
# You can't get into the last tennis ball without removing the balls ontop
# It's called LIFO(Last-In, First-Out)
# How to implement a stack (List)
# In the course of this course we would be using a LinkedList
# N/B: When dealing with stack it's case scenerio can be in two ways Horizontal or Vertical
# Horizontal method -: When adding to the end of the list and removing from the list it's O(1) & o(n) respectively
#                      When removing from the front of the list adding to and removing from the list is both O(1)
# Vertical method -: It's much better because we are now dealing with push and pop which adds to the top of the stack only and makes it O(1)
# When dealing with stach we only consider the top while for list we considered Head & Tail
# Illustration before adding to the constructor
top = {
    "value": 4,
    "next": None
}

# We start by building the stack constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating the stack class
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # print method to for a stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    # push to the stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    # pop out of a stack
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

# Method to print stack
my_stack = Stack(4)

my_stack.print_stack()


# Method to push to a stack
my_stack =  Stack(4)
my_stack.push(1)

my_stack.print_stack()


# Method to pop out of a stack
my_stack =  Stack(7)
my_stack.push(1)
my_stack.push(49)
my_stack.push(54)
my_stack.push(5)

print(my_stack.pop(), '\n')

my_stack.print_stack()






############################### Leetcode Exercises ################################

# 1.) STACK PUSH FOR STACK THAT USES LIST
# Instructions:
# Stack: Push for Stack That Uses List (⚡Interview Question)
# Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

# Remember: This Stack implementation uses a list instead of a linked list.
class Stack_Excercise:
    def __init__(self):
        self.stack_list = []
    
    def print_stack_list(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
        
    def size(self):
        return len(self.stack_list)
    
    def push(self, value):
        self.stack_list.append(value)


# 2.) STACK PARENTHESIS BALANCED 
# Instructions:
# Stack: Parentheses Balanced (⚡Interview Question)
# Check to see if a string of parentheses is balanced or not.

# By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.

# Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.


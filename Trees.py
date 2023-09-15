{
"value": 4,
"left": {
        "value": 3,
        "left": None,
        "right": None
       },
"right": {
        "value": 23,
          "left": None,
          "right": None
        }
}
# Terminologies when dealing with Trees Data Structure
# 1.) Full Tree - Every node either points to zero nodes or two nodes
# 2.) Perfect Tree - Any level in the that has any nodes is completely filled all the way across
# 3.) Complete Tree - You are filling the tree from left to right with no gaps
# 4.) Parent node - 
# 5.) Child node - 
# 6.) Leaf node - These are nodes without any children


# Binary Search Trees O(log n) Divide and conquer - It's very effecient 
# N.B we can also have O(n) in a BST but we treat lookup(), insert() and remove() as O(log n)
# Comparism between List and Binary Search Tree
#                 LinkedList            BinarySearchTree
# 1.) insert()     Good O(1)             Bad O(log n)
# 2.) lookup()     Bad O(n)              Good O(log n)
# 3.) remove()     Bad O(n)              Good O(log n)

# Building the constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class BinarySearchTree:
#     def __init__(self, value):
#         new_node = Node(value)
#         # when using trees we don't call it head rather we call it root so we create the root variable
#         self.root = new_node

# We can create our class in a way that you don't have to create a node as the tree is being created
# Instead you equate the root to None whereby you can add to the tree using the insert method
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # Creating an insert method
    def insert(self, value):
        # Create a new node with the given value.
        new_node = Node(value) 

        # If the tree is empty (root is None), set the new node as the root.
        if self.root is None:
            self.root = new_node 
            return True
        
         # Initialize a temporary pointer 'temp' starting from the root.
        temp = self.root 
    
        while (True):
            # If a node with the same value already exists, return False (no duplicates allowed).
            if new_node.value == temp.value:
                return False
            
            # If the new node's value is less than the current node's value:
            if new_node.value < temp.value:
                # If there's no left child, insert the new node as the left child.
                if temp.left is None:
                    temp.left = new_node 
                    return True
                # Move the temporary pointer to the left child.
                temp = temp.left
            else:
                # If the new node's value is greater than the current node's value:
                # If there's no right child, insert the new node as the right child.
                if temp.right is None:
                    temp.right = new_node 
                    return True
                # Move the temporary pointer to the right child.
                temp = temp.right 

    # Code A
    # Creating an insert method
    def contains(self, value):
        # If the tree is empty (root is None), return False.
        if self.root is None:
            return False
        
        # Initialize a temporary pointer 'temp' starting from the root.
        temp = self.root

        # Start a loop to traverse the tree.
        while temp is not None:
            # If the 'value' to search for is less than the current node's value,
            # move to the left child.
            if value < temp.value:
                temp = temp.left
            # If the 'value' to search for is greater than the current node's value,
            # move to the right child.  
            elif value > temp.value:
                temp = temp.right
            else:
                 # If the 'value' is equal to the current node's value, return True
                # because the value has been found in the tree.
                return True
            
        # If the loop completes without finding the 'value', return False.   
        return False
    
    # Code B
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


# Illustration for the insert method
# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)


# Illustration for the contains method
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52) 
my_tree.insert(82)


print(my_tree.contains(27))
print(my_tree.contains(17))

# If you want to run the both contains method comment one and run the other
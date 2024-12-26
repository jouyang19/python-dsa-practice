# BST: Insert
# Implement the insert method for the BinarySearchTree class that inserts a new node with a given value into the binary search tree.

# The method should perform the following tasks:

# Create a new instance of the Node class using the provided value.

# If the binary search tree is empty (i.e., self.root is None), set the root attribute of the BinarySearchTree class to point to the new node and return True.

# If the binary search tree is not empty, initialize a temporary variable temp to point to the root node, and then perform the following steps in a loop until the new node is inserted:

# If the value of the new node is equal to the value of the current node (stored in temp), return False, indicating that duplicate values are not allowed in the tree.

# If the value of the new node is less than the value of the current node, check if the left child of the current node is None:

# If it is, set the left child of the current node to the new node and return True.

# If it is not, update temp to point to the left child and continue the loop.

# If the value of the new node is greater than the value of the current node, check if the right child of the current node is None:

# If it is, set the right child of the current node to the new node and return True.

# If it is not, update temp to point to the right child and continue the loop.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ## WRITE INSERT METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    def insert(self, value):
        new_node = Node(value)
        if self.root == None: 
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value: 
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
                
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""
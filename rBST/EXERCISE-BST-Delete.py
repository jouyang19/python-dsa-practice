# rBST: Delete
# Write two Python functions for the BinarySearchTree class: delete_node and __delete_node.

# These functions should work together to delete a node with a given integer value from the binary search tree while maintaining its structure and ordering after deletion.

# delete_node(value): This function should take an integer value as input and call the __delete_node function with the root node of the binary search tree and the input value. It should then update the root of the binary search tree with the returned value from the __delete_node function.

# __delete_node(current_node, value): This function should take a Node object (current_node) and an integer value as input. It should be a recursive helper function that facilitates the node deletion process for the delete_node function. The function should have the following behavior:

# If the current_node is None, return None.

# If the input value is smaller than the value of the current_node, set the left child of the current_node to the result of calling __delete_node with the left child of the current_node and the input value.

# If the input value is larger than the value of the current_node, set the right child of the current_node to the result of calling __delete_node with the right child of the current_node and the input value.

# If the input value is equal to the value of the current_node, perform the deletion according to the following cases:

# If the current_node has no children, return None.

# If the current_node has only a left child, return the left child.

# If the current_node has only a right child, return the right child.

# If the current_node has both left and right children, find the minimum value in the right subtree of the current_node, replace the value of the current_node with the found minimum value, and then delete the node with the minimum value in the right subtree using a recursive call to __delete_node.

# Return the current_node after making the necessary updates.

# Your implementation should ensure that the binary search tree maintains its structure and ordering after the deletion operation.



# Please click on "Hints" (above) to see the pseudo-code.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
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


    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
 

    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

 
          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    ## WRITE DELETE_NODE METHODS HERE ##
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def __delete_node(self, current_node, value):
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.right == None:
                current_node = current_node.left
            elif current_node.left == None:
                current_node = current_node.right
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)



my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.delete_node(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)



"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""

# This code implements a binary search tree (BST), which is a binary tree data structure where each node has at most two child nodes, arranged in a way that the value of the node to the left is less than or equal to the parent node, and the value of the node to the right is greater than or equal to the parent node.

# The delete_node method is a public method to delete a node with a given value from the BST.

# The actual deletion logic is implemented in the private method __delete_node.

# The logic of the __delete_node method is as follows:

# If the current node is empty (None), it means the node with the given value is not found, so return None.

# If the value to delete is less than the current node's value, search in the left subtree.

# If the value to delete is greater than the current node's value, search in the right subtree.

# If the value to delete is equal to the current node's value, we have found the node to delete. There are three cases: a. If the node has no children, remove the node by returning None. b. If the node has only a left child or only a right child, remove the node by returning the existing child. c. If the node has both children, find the minimum value in the right subtree, replace the current node's value with that minimum value, and then delete the minimum value node in the right subtree.



# The reason we use self.root = self.__delete_node(self.root, value) instead of self.__delete_node(self.root, value) is to update the tree's root node after deletion. 

# This is necessary if the root node is the one being deleted or if its value is replaced with the minimum value from its right subtree.

# By assigning the result of self.__delete_node(self.root, value) to self.root, we ensure that the root node is updated accordingly, maintaining the integrity of the tree structure.





# Code with inline comments:



# def __delete_node(self, current_node, value):
#     # Return None if the current node is None
#     if current_node == None:
#         return None
#     # Traverse the left subtree if value is smaller
#     if value < current_node.value:
#         current_node.left = self.__delete_node(current_node.left, value)
#     # Traverse the right subtree if value is larger
#     elif value > current_node.value:
#         current_node.right = self.__delete_node(current_node.right, value)
#     # If value is found, delete the node
#     else:
#         # Case 1: No children, return None to delete
#         if current_node.left == None and current_node.right == None:
#             return None
#         # Case 2: No left child, return right child
#         elif current_node.left == None:
#             current_node = current_node.right
#         # Case 3: No right child, return left child
#         elif current_node.right == None:
#             current_node = current_node.left
#         # Case 4: Two children, find min in right subtree
#         else:
#             sub_tree_min = self.min_value(current_node.right)
#             current_node.value = sub_tree_min
#             current_node.right = self.__delete_node(current_node.right, sub_tree_min)
#     # Return the current node after deletion
#     return current_node
 
# def delete_node(self, value):
#     # Call the helper method to delete the node
#     # You may see other implementations that write it this way:
#     # self.__delete_node(self.root, value)
#     # but that way will not work when removing the root node
#     self.root = self.__delete_node(self.root, value)
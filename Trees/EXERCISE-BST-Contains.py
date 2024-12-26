# BST: Contains
# Implement the contains method for the BinarySearchTree class that checks if a node with a given value exists in the binary search tree.

# The method should perform the following tasks:

# Initialize a temporary variable temp to point to the root node of the binary search tree.

# Use a loop to traverse the binary search tree until the target value is found or the end of the tree is reached:

# If the target value is less than the value of the current node (stored in temp), update temp to point to the left child and continue the loop.

# If the target value is greater than the value of the current node, update temp to point to the right child and continue the loop.

# If the target value is equal to the value of the current node, return True, indicating that the target value exists in the tree.

# If the loop ends without finding the target value, return False, indicating that the target value does not exist in the tree.

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

    ## WRITE CONTAINS METHOD HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    # def contains(self, value):
    #     if self.root is None:
    #         return False
    #     temp = self.root
    #     while temp:
    #         if value == temp.value:
    #             return True
    #         if value < temp.value:
    #             if temp.left is None:
    #                 return False
    #             temp = temp.left
    #         else:
    #             if temp.right is None:
    #                 return False
    #             temp = temp.right

# solution
    def contains(self, value):
        # This part of code not needed because if it is None, it will eventually return False
        # if self.root is None:
        #     return False 
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""
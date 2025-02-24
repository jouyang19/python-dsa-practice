"""
DFS PostOrder
Write a function called dfs_post_order that performs a Depth-First Search (DFS) traversal on a binary tree using the Post-Order approach.

The function should perform the following tasks:

Create an empty list called results to store the visited nodes in order.

Define a nested function called traverse that takes a current_node as an argument.

In the traverse function, perform the following tasks:

If the current_node has a left child, recursively call the traverse function with the left child as an argument.

If the current_node has a right child, recursively call the traverse function with the right child as an argument.

Append the value of the current_node to the results list.

Call the traverse function with the root of the binary tree as the initial argument.

Return the results list, containing the values of the nodes in the order they were visited during the Post-Order Depth-First Search traversal.
"""

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
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    ### WRITE DFS_POST_ORDER METHOD HERE ###
    #                                      #
    #                                      #
    #                                      #
    #                                      #
    ########################################
    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results




my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_post_order())



"""
    EXPECTED OUTPUT:
    ----------------
    [18, 27, 21, 52, 82, 76, 47]

 """


"""
The dfs_post_order method in the BinarySearchTree class performs a Depth-First Search traversal of the binary search tree post-order. The post-order traversal visits the left child first, then the right child, and finally the current node.

The dfs_post_order method starts by creating an empty list called results that will be used to store the values of the visited nodes. Then, the method defines a nested function called traverse that takes a current_node argument. The traverse function recursively calls itself to traverse the left child of the current_node, then recursively calls itself to traverse the right child of the current_node, and finally appends the value of the current_node to the results list.

The method then calls the traverse function with the root node of the tree to start the post-order traversal. The traverse function recursively visits each node in the tree post-order, appending the value of each visited node to the results list after visiting its children. Finally, the dfs_post_order method returns the results list, which contains the values of all nodes in the binary search tree post-order.





Code with inline comments:



def dfs_post_order(self):
    results = []  # create an empty list to store the values of visited nodes
 
    def traverse(current_node):
        # if the current node has a left child, recursively traverse it
        if current_node.left is not None:
            traverse(current_node.left)
 
        # if the current node has a right child, recursively traverse it
        if current_node.right is not None:
            traverse(current_node.right)
 
        # append the value of the current node to the results list
        results.append(current_node.value)
 
    # start the post-order traversal from the root of the tree
    traverse(self.root)
 
    # return the list of visited node values
    return results

"""
# BFS (Breadth First Search)
# Write a function called BFS that performs a Breadth-First Search traversal on a binary tree.

# The function should perform the following tasks:

# Initialize the current_node variable with the root of the binary tree.

# Create an empty list called queue to store nodes for processing, and another empty list called results to store the visited nodes in order.

# Append the current_node to the queue.

# Implement a loop that continues until the queue is empty:

# Set current_node to the first element in the queue, and remove this element from the queue.

# Append the value of current_node to the results list.

# If the current_node has a left child, append it to the queue.

# If the current_node has a right child, append it to the queue.

# Return the results list, containing the values of the nodes in the order they were visited during the Breadth-First Search traversal.

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
  
    ### WRITE BFS METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
    def BFS(self):
        current_node = self.root
        results = []
        queue = []
        queue.append(self.root) # append the root first, to get the loop going
        while len(queue): # loop will keep running as long as there is something in the tree to search for and add to queue
            current_node = queue.pop(0) # FIFO, not LIFO, hence index of 0. Queue has FIFO while a list has LIFO
            results.append(current_node.value) # make sure to append to results, not queue. And append the value, not the whole node.
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """


# The BFS method performs a Breadth-First Search traversal of the binary search tree.

# The method starts at the root of the tree and adds it to a queue data structure.

# Then, the method loops over the elements in the queue, removing the first element in the queue, appending its value to a results list, and adding its left and right child (if they exist) to the queue.

# The method continues this process until the queue is empty, at which point it returns the results list containing the values of all nodes in the binary search tree in breadth-first order.

# The BFS method uses a queue to keep track of the nodes to visit in a first-in, first-out (FIFO) order, which is the main characteristic of the BFS algorithm.

# The method removes the first element in the queue using the pop(0) method, which ensures that the next element to be visited is always the one that was added first.

# The BFS algorithm traverses the tree level-by-level, visiting all nodes at a particular level before moving on to the next level. The BFS method in this implementation achieves this by using a queue to keep track of nodes that have been visited, but not processed, in the order they were visited.     





# Code with inline comments:



# def BFS(self):
#     # set current_node to the root of the tree
#     current_node = self.root
    
#     # create an empty queue to store nodes to visit
#     queue = []
    
#     # create an empty list to store the values of visited nodes
#     results = []
    
#     # add the root node to the queue
#     queue.append(current_node)
 
#     # continue until all nodes have been visited
#     while len(queue) > 0:
#         # remove the first node from the queue
#         current_node = queue.pop(0)
        
#         # add the value of the visited node to the results list
#         results.append(current_node.value)
        
#         # if the visited node has a left child, add it to the queue
#         if current_node.left is not None:
#             queue.append(current_node.left)
        
#         # if the visited node has a right child, add it to the queue
#         if current_node.right is not None:
#             queue.append(current_node.right)
 
#     # return the list of visited node values
#     return results



                



 
# Queue: Dequeue
# Implement the dequeue method for the Queue class that removes the first node from the queue and returns it.

# The method should perform the following tasks:

# If the queue is empty (i.e., the length is 0), return None.

# Store a reference to the current first node in a temporary variable, temp.

# If the queue has only one node (i.e., the length is 1), set both the first and last attributes of the Queue class to None.

# If the queue has more than one node, perform the following steps:

# Update the first attribute of the Queue class to point to the next node in the queue.

# Set the next attribute of the removed node (stored in the temporary variable) to None.

# Decrement the length attribute of the Queue class by 1.

# Return the removed node (stored in the temporary variable).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    ## WRITE DEQUEUE METHOD HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first 
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            self.length -= 1 
        return temp
            
 

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""
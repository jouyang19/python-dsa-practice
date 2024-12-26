# Stack:Pop
# Implement the pop method for the Stack class that removes the top node from the stack and returns it.

# The method should perform the following tasks:

# If the stack is empty (i.e., the height is 0), return None.

# Store a reference to the current top node in a temporary variable, temp.

# Update the top attribute of the Stack class to point to the next node in the stack.

# Set the next attribute of the removed node (stored in the temporary variable) to None.

# Decrement the height attribute of the Stack class by 1.

# Return the removed node (stored in the temporary variable).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
    def pop(self):
        if self.top == 0: # edge case when there are no nodes
            return None
        temp = self.top # save location of top
        self.top = self.top.next # to move the top to next node
        temp.next = None # to remove the top most node 
        self.height -= 1
        return temp # return popped node

    

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""
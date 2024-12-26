class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))

    #   +===================================================+
    #   |                  WRITE YOUR CODE HERE             |
    #   | Description:                                      |
    #   | - This method removes all nodes with duplicate    |
    #   |   values from the linked list.                    |
    #   | - It keeps track of seen values with a set.       |
    #   | - If a value is repeated, it is skipped over by   |
    #   |   changing the 'next' pointer of the previous     |
    #   |   node, effectively removing the duplicate.       |
    #   | - The list's length is adjusted for each removed  |
    #   |   duplicate.                                      |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We maintain a 'previous' node as a reference    |
    #   |   to re-link the list when skipping duplicates.   |
    #   | - The 'current' node iterates through the list.   |
    #   | - The 'values' set holds unique items seen so far.|
    #   +===================================================+
    def remove_duplicates(self):
        values = set()
        curr = self.head
        prev = None
        while curr:
            if curr.value in values:
                prev.next = curr.next
                self.length -= 1
            else:
                values.add(curr.value)
                prev = curr
            curr = curr.next
            
# For the optimal solution you will want to use a Set (you can read more about Sets here):

# I have also included an implementation that does not use a Set at the bottom of this explanation.

# Either solution will work but the one with Sets is O(n) while the other is O(n^2) time complexity.



#     def remove_duplicates(self):
#             values = set()
#             previous = None
#             current = self.head
#             while current:
#                 if current.value in values:
#                     previous.next = current.next
#                     self.length -= 1
#                 else:
#                     values.add(current.value)
#                     previous = current
#                 current = current.next




# Let's break down the remove_duplicates function.

# This function aims to remove any duplicate nodes from a linked list. For instance, if you have a linked list:

# 3 → 5 → 3 → 7 → 8 → 5 → 9
# After removing duplicates, it should look like:

# 3 → 5 → 7 → 8 → 9


# Method Walkthrough:

# def remove_duplicates(self):


# Initialize a set to store unique values:

# values = set()
# We're using a set (values) because checking membership in a set is typically O(1), making it efficient for this operation. As we traverse the list, we'll add each encountered node's value to this set.



# Setup initial pointers:

# previous = None
# current = self.head
# The current pointer will traverse through the list, while previous will keep track of the last unique node.



# Iterate through the list to remove duplicates:

# while current:
# This loop will traverse each node in the linked list.



# Check if the current node's value is in our set of seen values:

# if current.value in values:
# If this condition is true, it means we've seen this value before, and therefore, the current node is a duplicate.



# Remove the current node from the list:

#     previous.next = current.next
#     self.length -= 1
# If the current node's value is a duplicate, we'll bypass it by pointing the next attribute of the previous node directly to current.next, effectively skipping over the current node. We then decrement the length of the linked list since we've removed a node.



# Otherwise, if the value is unique (not seen before):

# else:
#     values.add(current.value)
#     previous = current
# If we haven't seen the current value before, we add it to our set (values) and move the previous pointer to point at the current node since it's unique.



# Move to the next node:

#     current = current.next
# We update the current pointer to move on to the next node in the list for further processing.



# Conclusion: The remove_duplicates method efficiently iterates through the linked list, maintaining a set of seen values. If a value is repeated, the node containing that value gets removed from the list. By the end of the function, all duplicate nodes in the linked list will have been removed. In our example, repeated nodes with values 3 and 5 are removed, leaving us with a linked list of unique values: 3 → 5 → 7 → 8 → 9.





# Code with inline comments:



# def remove_duplicates(self):
#     # 1. Initialize a set called 'values' to store unique node values.
#     values = set()
    
#     # 2. Initialize 'previous' to None. 
#     # This will point to the last node we've seen that had a unique value.
#     previous = None
    
#     # 3. Start at the head of the linked list.
#     current = self.head
 
#     # 4. Traverse through the linked list.
#     while current:
#         # 4.1. Check if the value of the current node is already in the set.
#         if current.value in values:
#             # 4.1.1. If yes, bypass this node by pointing the next of 
#             # 'previous' to the next of 'current'.
#             previous.next = current.next
            
#             # 4.1.2. Decrement the length of the list.
#             self.length -= 1
#         else:
#             # 4.2. If not, add the value to the set.
#             values.add(current.value)
            
#             # 4.2.1. Update the 'previous' to point to 'current' now.
#             previous = current
 
#         # 4.3. Move to the next node in the list.
#         current = current.next


# You can also do this without a Set but this will change the Big O from O(n) to O(n^2):

# A Set is a data structure that we will learn more about later in the course.

# Here is the solution without using a Set:



#     def remove_duplicates(self):
#         current = self.head
#         while current:
#             runner = current
#             while runner.next:
#                 if runner.next.value == current.value:
#                     runner.next = runner.next.next
#                     self.length -= 1
#                 else:
#                     runner = runner.next
#             current = current.next
            
            
            


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")

# Test 1: List with no duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 2: List with some duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
test_remove_duplicates(ll, [1, 2, 3])

# Test 3: List with all duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(1)
test_remove_duplicates(ll, [1])

# Test 4: List with consecutive duplicates
ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 5: List with non-consecutive duplicates
ll = LinkedList(1)
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(4)
test_remove_duplicates(ll, [1, 2, 3, 4])

# Test 6: List with duplicates at the end
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
test_remove_duplicates(ll, [1, 2, 3])

# Test 7: Empty list
ll = LinkedList(None)
ll.head = None  # Directly setting the head to None
ll.length = 0   # Adjusting the length to reflect an empty list
test_remove_duplicates(ll, [])

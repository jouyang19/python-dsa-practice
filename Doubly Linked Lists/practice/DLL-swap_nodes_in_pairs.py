# DLL: Swap Nodes in Pairs ( ** Interview Question)
# You are given a doubly linked list.

# Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

# Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

# Example:

# 1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

# Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

# Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    # WRITE SWAP_PAIRS METHOD HERE #
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    # def swap_pairs(self):
    #     if self.length <= 1:
    #         return False
    #     temp = self.head
    #     after = self.head.next
    #     before = None
    #     self.head = after
    #     while temp and after:
    #         next_pair = after.next
            
    #         temp.next = after.next
    #         temp.prev = after
    #         after.next = temp
    #         after.prev = before
            
    #         before = temp
    #         temp = next_pair
    #         after = temp.next if temp else None
            
    #         if temp:
    #             temp.prev = before
    #     return True
    
    def swap_pairs(self):
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
        while self.head and self.head.next is not None:
            first_node = self.head
            second_node = self.head.next
            previous_node.next = second_node
            first_node.next = second_node.next 
            second_node.next = first_node
            second_node.prev = previous_node 
            first_node.prev = second_node
            if first_node.next is not None:
                first_node.next.prev = first_node
            self.head = first_node.next
            previous_node = first_node
        self.head = dummy_node.next
        if self.head:
            self.head.prev = None
            
# Pseudo Code:

# As you work through the pseudo-code, I recommend sketching the nodes, pointers, and each step on paper. This visual representation will greatly aid in understanding and tracking the process.


# Initialize a dummy node to simplify the swapping process.

# Create a dummy_node with value 0.

# Set dummy_node.next to self.head.

# Initialize previous_node to dummy_node.

# Loop through the list as long as there's a pair of nodes to swap.

# While self.head and self.head.next are not None, do the following:

# 2.1. Identify the first node in the pair to be swapped. - Set first_node to self.head.

# 2.2. Identify the second node in the pair to be swapped. - Set second_node to self.head.next.

# 2.3. Connect 'previous_node's 'next' pointer to 'second_node'. - Set previous_node.next to second_node.

# 2.4. Connect 'first_node' to the node after 'second_node'. - Set first_node.next to second_node.next.

# 2.5. Connect 'second_node' back to 'first_node', effectively swapping them. - Set second_node.next to first_node.

# 2.6. Adjust the 'prev' pointers to maintain the doubly-linked structure. - Set second_node.prev to previous_node. - Set first_node.prev to second_node.

# 2.7. If there's a node after the current pair, set its 'prev' to point back to 'first_node'. - If first_node.next is not None, set first_node.next.prev to first_node.

# 2.8. Move 'head' to the node after the current pair for the next iteration. - Set self.head to first_node.next.

# 2.9. Update 'previous_node' to 'first_node' for the next pair. - Set previous_node to first_node.

# Reset the list's head to start at the node after 'dummy_node'.

# Set self.head to dummy_node.next.

# Ensure the new head's 'prev' is None, indicating the start of the list.

# If self.head is not None, set self.head.prev to None.





# Explained another way:



# Our swap_pairs function operates like a road crew assigned to swap the positions of each pair of street signs on a two-way street. The dummy_node serves as a temporary post that helps the crew keep track of the street's starting point.

# The crew progresses down the street, working on pairs of signs, represented by first_node and second_node. This happens as long as self.head and self.head.next are not null. The aim is to swap these two signs while adjusting their 'next' and 'prev' pointers to maintain the street's correct layout.

# Initially, the crew ensures that the previous sign or post (previous_node) now points to second_node rather than first_node (previous_node.next = second_node). Then they adjust first_node so that its 'next' pointer targets whatever sign comes after second_node (first_node.next = second_node.next). Finally, they have second_node point back to first_node (second_node.next = first_node).

# But since it's a two-way street, the 'prev' pointers also need to be updated. The 'prev' pointer of second_node is set to point back to the previous sign (previous_node) (second_node.prev = previous_node). The 'prev' pointer of first_node is adjusted to point to second_node (first_node.prev = second_node). If there happens to be another sign after first_node, its 'prev' pointer is set to first_node (first_node.next.prev = first_node).

# After each pair of signs has been swapped, the crew moves on to the next pair. They set the 'head' to the sign following first_node (self.head = first_node.next) and adjust previous_node to first_node for the next iteration (previous_node = first_node).

# At the end of the operation, they mark the official start of the street to be the sign immediately after dummy_node (self.head = dummy_node.next). They also ensure that the 'prev' pointer of this new starting sign is null (self.head.prev = None), signaling the start of the street.

# With this, every pair of signs on the street has been swapped. For instance, if the original order was 1, 2, 3, 4, it would now be 2, 1, 4, 3. Despite the swaps, the 'next' and 'prev' pointers are correctly maintained, allowing for proper traffic flow in both directions.



# Explained yet another way:

# Think of the DoublyLinkedList as a group of friends standing in line for ice cream. Each friend is a 'Node', and they are each holding a card with a number ('value') on it. In addition, they each have two strings in their hands— one labeled 'next' and the other labeled 'prev.' These strings are tied to the friends directly in front of and behind them in line.

# The 'head' is the friend at the very start of the line. When you append a new friend to the list, they join the end of the line. They hold a new number card and tie their 'next' and 'prev' strings to the friend who was previously at the end of the line and to no one, respectively (since there's no friend behind them yet).

# Now, the swap_pairs function operates like a game that the friends play. The objective is for every adjacent pair of friends to swap places in line. The friend who was second will move to the first place, and vice versa, all the way down the line. They must also untie and re-tie their 'next' and 'prev' strings to the correct friends as they move.

# In the code, dummy_node is like an extra friend who helps us remember the start of the line. The variable previous_node functions like a pointer, showing us which friend we're currently examining in the line.

# The code progresses through each pair of friends in line (while self.head and self.head.next). It helps them swap places and re-tie their strings correctly, then moves to the next pair (self.head = first_node.next).

# After everyone has swapped places, dummy_node lets us know who the new first friend in line is (self.head = dummy_node.next). We also ensure that the first friend's 'prev' string is not tied to anyone else, since no friend stands before the first in line.

# So, after the swap_pairs function runs, if your friends were initially in line as 1, 2, 3, 4, they will now be in the sequence 2, 1, 4, 3.
    # =======================================================================
# In this function, the goal is to swap every two adjacent nodes in the doubly linked list.

# Given a doubly linked list like:

# 1 <-> 2 <-> 3 <-> 4

# After performing the swap_pairs operation, it should look like:

# 2 <-> 1 <-> 4 <-> 3



# Method Walkthrough:

# def swap_pairs(self):


# Initialize a dummy node and connect it to head for easier manipulation:

# dummy_node = Node(0)
# dummy_node.next = self.head
# This dummy node simplifies the swapping process, especially at the beginning of the list. We link the dummy's next to the head.



# Set up the previous pointer:

# previous_node = dummy_node
# previous_node pointer always points to the node just before the first node in the pair we're about to swap.



# Iterate through the list as long as there are at least two nodes left to swap:

# while self.head and self.head.next:


# Assign the two nodes to be swapped to first_node and second_node:

# first_node = self.head
# second_node = self.head.next


# Swapping logic:
# a. Point previousNode's next to second_node:

# previous_node.next = second_node
# previous_node should point to the second node of the pair after swapping.



# b. Link the end of our swapped pair to the rest of the list:

# first_node.next = second_node.next
# This ensures that after swapping, the list remains intact.



# c. Make the actual swap by reversing their next pointers:

# second_node.next = first_node


# Update the previous pointers for a doubly linked list:

# a. Link the prev pointer of second_node:

# second_node.prev = previous_node


# b. Update the prev pointer for the first_node:

# first_node.prev = second_node


# c. Ensure that the node after our swapped pair has its prev updated:

# if first_node.next:
#     first_node.next.prev = first_node


# Move the head pointer two nodes ahead for the next iteration:

# self.head = first_node.next
# This is essential since we've swapped the current pair and need to move to the next pair.



# Update the previous_node pointer to point to the first_node after the swap:

# previous_node = first_node
# As we move on to the next pair, our previous pointer should move two nodes ahead, but since we've swapped them, it now needs to point to what was originally the first node of our pair.



# Finally, reset the head of the list:

# self.head = dummy_node.next
# Once we've swapped all possible pairs, we adjust our head to point to the node following our dummy node.



# Ensure the new head's previous pointer is None:

# if self.head:
#     self.head.prev = None
# After all swaps, it's crucial to reset the prev pointer of the head to ensure the integrity of the doubly linked list.



# Conclusion: The swap_pairs function effectively swaps adjacent nodes in pairs for a doubly linked list. By employing a dummy node, we simplify the task of swapping, especially at the beginning of the list. After all operations, we ensure the head is correctly placed, and the previous pointers are updated to retain the doubly linked list's structure. In our given example, the nodes of 1 <-> 2 <-> 3 <-> 4 get swapped to become 2 <-> 1 <-> 4 <-> 3.





# Code with inline comments:



# def swap_pairs(self):
#     # Step 1: Initialize a dummy node to act as a placeholder
#     # for the start of the list.
#     dummy_node = Node(0)
 
#     # Connect this dummy node to the actual head of the list.
#     # This simplifies the swapping process.
#     dummy_node.next = self.head
 
#     # Step 2: Initialize 'previous_node' to 'dummy_node'.
#     # This helps us remember the node just before the pair
#     # we are about to swap.
#     previous_node = dummy_node
 
#     # Step 3: Loop through the list as long as there are pairs
#     # of nodes available to swap.
#     while self.head and self.head.next:
 
#         # Identify the first node in the pair to be swapped.
#         first_node = self.head
 
#         # Identify the second node in the pair to be swapped.
#         second_node = self.head.next
 
#         # Update 'previous_node' to point to 'second_node',
#         # effectively skipping over 'first_node'.
#         previous_node.next = second_node
 
#         # Connect 'first_node' to the node that comes after
#         # 'second_node'. This ensures we don't lose the
#         # rest of the list.
#         first_node.next = second_node.next
 
#         # Swap 'first_node' and 'second_node' by connecting
#         # 'second_node' back to 'first_node'.
#         second_node.next = first_node
 
#         # Update the 'prev' pointers for both 'first_node'
#         # and 'second_node' to maintain the doubly-linked
#         # structure.
#         second_node.prev = previous_node
#         first_node.prev = second_node
 
#         # If there's a node after 'first_node', update its
#         # 'prev' to point back to 'first_node'.
#         if first_node.next:
#             first_node.next.prev = first_node
 
#         # Move the 'head' to the node just after 'first_node'
#         # to prepare for the next iteration.
#         self.head = first_node.next
 
#         # Update 'previous_node' to point to 'first_node'
#         # for the next pair to swap.
#         previous_node = first_node
 
#     # After the loop, set the new head of the list to the
#     # node that comes after 'dummy_node'.
#     self.head = dummy_node.next
 
#     # Make sure the new head's 'prev' is set to None, as it
#     # is now the first node in the list.
#     if self.head:
#         self.head.prev = None



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""
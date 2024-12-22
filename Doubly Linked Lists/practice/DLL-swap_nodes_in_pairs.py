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
    def swap_pairs(self):
        # Handle empty or single node lists
        if self.length <= 1:
            return False
            
        # Initialize pointers
        temp = self.head
        after = self.head.next
        before = None
        
        # Update head to point to second node
        self.head = after
        
        while temp and after:
            # Save next pair
            next_pair = after.next
            
            # Swap the current pair
            temp.next = after.next
            temp.prev = after
            after.next = temp
            after.prev = before
            
            if next_pair:
                next_pair.prev = temp
            
            # Update before pointer
            before = temp
            
            # Move to next pair
            temp = next_pair
            after = temp.next if temp else None
            
            # # Connect with previous pair
            # if temp:
            #     temp.prev = before

        return True
            


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
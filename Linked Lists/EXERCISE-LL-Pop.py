class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    ### WRITE POP METHOD HERE ###
    #                           #
    #                           #
    #                           #
    #                           #
    #############################
    def pop(self):
        # checks if the list is empty
        if self.length == 0:
            return None
        # initialize temp and pre to head
        temp = self.head
        prev = self.head
        # iterate until the last node
        while temp.next is not None:
            prev = temp
            temp = temp.next
        # set the new tail to the previous node
        self.tail = prev
        # remove link to the removed node
        self.tail.next = None
        # decrement linked list length by 1
        self.length -= 1
        # check if the list is now empty
        if self.length == 0:
            # set head and tail to None
            self.head = None
            self.tail = None
        # return the removed node
        return temp
 
# Alternate Solution
    #  def pop(self):
    #  # this handles edge case if there are no nodes present
    #     if self.length == 0:
    #         return None
    #   # this handles edge case if there is only 1 node
    #     if self.length == 1:
    #         temp = self.head
    #         self.head = None
    #         self.tail = None
    #         self.length -= 1
    #         return temp
    #     else:
    #         # set the temp pointer to the beginning of linked list
    #         temp = self.head
    #         # traverse until we find the second-to-last node where temp.next.next is None.
    #         while temp.next.next is not None: 
    #             temp = temp.next
    #         # save last node in last_node
    #         last_node = temp.next
    #         # set temp.next to None to remove the last node
    #         temp.next = None
    #         # update tail to point to temp (the new last node)
    #         self.tail = temp
    #         # decrease length to reflect the new change
    #         self.length -= 1
    #         # return the removed node's value
    #         return last_node


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""


##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")


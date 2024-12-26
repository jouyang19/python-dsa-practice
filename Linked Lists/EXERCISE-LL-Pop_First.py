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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    ## WRITE POP_FIRST METHOD HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
# set prev to self.head then set head to next node, return prev 
# 1 node edge case: set prev to the one only node, set self.head and tail to None and return prev
# 0 node edge case: return None

# My solution
    # def pop_first(self):
    #     if self.head is None:
    #         return None
    #     if self.length == 1:
    #         prev = self.head 
    #         self.head = None
    #         self.tail = None
    #         self.length -= 1
    #         return prev
    #     else: 
    #         prev = self.head
    #         self.head = self.head.next
    #         prev.next = None
    #         self.length -= 1
    #         if self.length == 0:
    #             self.tail = None
    #         return prev

    def pop_first(self):
        
        # check if the linked list is empty, if it is, return None
        if self.length == 0:
            return None
        
        # save a reference to the current head node
        temp = self.head
        
        # update the head to the second node in the list
        self.head = self.head.next
        
        # disconnect the removed node from the list by removing the reference to it
        temp.next = None
        
        # decrease the length of the linked list by 1-
        self.length -= 1
        
        # in the case that the linked list started with 1 node and we popped, we check if the linked list is now empty, and if it is, self.head should already be None, however, self.tail is not updated and should now be set to None
        if self.length == 0:
            self.tail = None
            
        # return the removed node
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""

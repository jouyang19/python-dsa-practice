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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        # check if index is out of bounds
        if index < 0 or index > self.length:
            return False
        # if index is 0, prepend the value
        if index == 0:
            return self.prepend(value)
        # if the index is at the end, append the value
        if index == self.length:
            return self.append(value)
        # create new node
        new_node = Node(value)
        # get node just before insertion point (why? because the insertion point will be the new_node's next)
        temp = self.get(index - 1)
        # set new_node's next to temp's next
        new_node.next = temp.next
        # update temp's next to the new_node
        temp.next = new_node
        # update LL length
        self.length += 1   
        # return True as node inserted successfully
        return True  

    ## WRITE REMOVE METHOD HERE ##
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    # we'll need the previous node before index node, that previous node should point to the index node's next. Remove 1 from self.length of linked list class object instance. We also need to make sure index is not out of range.
    # def remove(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     if index == 0:
    #         # temp = self.head
    #         # self.head = self.head.next
    #         # temp.next = None
    #         # self.length -= 1
    #         # return temp
    #         return self.pop_first()
    #     if index == self.length - 1:
    #         # temp = self.head
    #         # pre = self.head
    #         # while(temp.next):
    #         #     pre = temp
    #         #     temp = temp.next
    #         # self.tail = pre
    #         # self.tail.next = None
    #         # self.length -= 1
    #         # if self.length == 0:
    #         #     self.head = None
    #         #     self.tail = None
    #         # return temp
    #         return self.pop()
    #     curr = self.head
    #     prev = self.head
    #     for _ in range(index):
    #         prev = curr
    #         curr = curr.next
    #     prev.next = curr.next
    #     curr.next = None
    #     self.length -= 1
    #     return curr
    
    def remove(self, index):
        # check if index is out of bounds and since we are returning the node's value, return None
        if index < 0 or index >= self.length:
            return None
        # remove and return the first node
        if index == 0:
            return self.pop_first()
        # remove and return the last node
        if index == self.length - 1:
            return self.pop()
        # get the previous node
        pre = self.get(index - 1)
        # set the cur to the node to be removed
        cur = pre.next
        # update the pre.next to skip the removed node
        pre.next = cur.next
        # disconnect the removed node 
        cur.next = None
        # decrement the list length
        self.length -= 1
        # return the removed node
        return cur
    
    



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL before remove():')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() in middle:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(0).value)
print('LL after remove() of first node:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() of last node:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    LL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    LL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    LL after remove() of last node:
    2
    4

"""


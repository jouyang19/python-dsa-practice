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
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        # create a new node with the given value
        new_node = Node(value)
        
        #################################
        # FINISH WRITING APPEND METHOD  #
        # INSERT IF/ELSE STATEMENT HERE #
        #################################
        # Check to see if the linked list is empty
        if self.head is None:
            # if it is, point both head and tail at the new_node
            self.head = new_node
            self.tail = new_node
        else: # if linked list is not empty
            # point the next pointer of last node to new node
            self.tail.next = new_node
            # point tail to new node
            self.tail = new_node
        
        self.length += 1 # increment length of linked list
        return True




my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""

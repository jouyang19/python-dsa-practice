class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    #  WRITE IS_PALINDROME METHOD HERE  #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        prev = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        first_half = self.head
        second_half = prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
            
        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(1)

print('my_linked_list is_palindrome:')
print(my_linked_list.is_palindrome())

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)

print('\nmy_linked_list_2 is_palindrome: ')
print(my_linked_list_2.is_palindrome())


"""
    EXPECTED OUTPUT:
    ----------------
    
    my_linked_list is_palindrome:
    True

    my_linked_list_2 is_palindrome:
    False
    
"""


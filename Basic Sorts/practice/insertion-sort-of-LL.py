"""Insertion Sort of LL ( ** Interview Question)
Assignment:

Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the insertion sort algorithm.

The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list.

You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.



Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.

The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.

The method then iterates through each remaining node in the unsorted part of the list.

For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value with the values of the other nodes in the sorted part of the list.

Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.

After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.



Constraints:

The linked list can contain duplicates.

The method should be implemented in the LinkedList class.

The method should not use any additional data structures to sort the linked list.

"""

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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE INSERTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
                    
    def insertion_sort(self):
        if self.length < 2: 
            return
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        sorted_list_cursor = sorted_list_head
        unsorted_list_cursor = unsorted_list_head
        while unsorted_list_head:
            unsorted_list_cursor = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if unsorted_list_cursor.value < sorted_list_head.value:
                unsorted_list_cursor.next = sorted_list_head
                sorted_list_head = unsorted_list_cursor
            else:
                sorted_list_cursor = sorted_list_head # reset sorted list's pointer to head for every iteration of unsorted list item
                while sorted_list_cursor.next and unsorted_list_cursor.value > sorted_list_cursor.next.value: # for each sorted item check if the currently selected unsorted item is less than the unsorted item.
                    sorted_list_cursor = sorted_list_cursor.next # while checking, loop through sorted list items
                unsorted_list_cursor.next = sorted_list_cursor.next
                sorted_list_cursor.next = unsorted_list_cursor
                
        self.head = sorted_list_head
        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp
                    
                
    




my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

"""
This code implements the insertion sort algorithm to sort the nodes in a singly linked list in ascending order.

Here's how it works:



First, the function checks if the length of the linked list is less than 2. If it is, then the list is already sorted, and the function returns.

Next, the function sets the sorted_list_head pointer to the head of the linked list, and the unsorted_list_head pointer to the next node after the head.

The sorted_list_head pointer is then disconnected from the rest of the list by setting its next attribute to None.

The function enters a loop where it iterates through each remaining node in the unsorted part of the list. For each node:

The node is temporarily saved in the current variable, and the unsorted_list_head pointer is moved to the next node.

If the current node is smaller than the first node in the sorted part of the list (i.e., the sorted_list_head node), then the current node becomes the new sorted_list_head node.

Otherwise, the function searches through the sorted part of the list to find the correct position to insert the current node. The search is done using the search_pointer variable, which initially points to the sorted_list_head node. The search_pointer variable is moved along the sorted part of the list until it reaches the last node that is smaller than the current node, or until it reaches the end of the sorted part of the list. Once the correct position is found, the current node is inserted into the sorted part of the list.

Finally, the head and tail attributes of the linked list are updated to reflect the new order of the nodes in the list. This is done by setting the head attribute to the new sorted_list_head node, and by iterating through the list to find the new tail node.





Code with inline comments:



def insertion_sort(self):
    # Check if the length of the list is less than 2
    if self.length < 2:
        return
    
    # Set the pointer to the first element of the sorted list
    sorted_list_head = self.head
    
    # Set the pointer to the second element of the list
    unsorted_list_head = self.head.next
    
    # Remove the first element from the sorted list
    sorted_list_head.next = None
    
    # Iterate through the unsorted list
    while unsorted_list_head is not None:
        # Save the current element
        current = unsorted_list_head
        
        # Move the pointer to the next element in the unsorted list
        unsorted_list_head = unsorted_list_head.next
        
        # Insert the current element into the sorted list
        if current.value < sorted_list_head.value:
            # If the current element is smaller than the first element 
            # in the sorted list, it becomes the new first element
            current.next = sorted_list_head
            sorted_list_head = current
        else:
            # Otherwise, search for the appropriate position to insert the current element
            search_pointer = sorted_list_head
            while search_pointer.next is not None and current.value > search_pointer.next.value:
                search_pointer = search_pointer.next
            current.next = search_pointer.next
            search_pointer.next = current
    
    # Update the head and tail of the list
    self.head = sorted_list_head
    temp = self.head
    while temp.next is not None:
        temp = temp.next
    self.tail = temp
    """
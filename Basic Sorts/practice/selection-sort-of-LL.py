"""Selection Sort of LL ( ** Interview Question)
Assignment:

Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list in ascending order using the selection sort algorithm. The method should update the head and tail pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the input linked list will contain only integers. You should not use any additional data structures to sort the linked list.



Input:

The LinkedList object containing a linked list with unsorted elements (self).



Output:

None. The method sorts the linked list in place.



Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The selection sort algorithm works by repeatedly finding the smallest element in the unsorted part of the list and swapping it with the first element in the unsorted part of the list.

The method starts with the entire linked list being the unsorted part of the list.

For each pass through the unsorted part of the list, the method iterates through each element to find the smallest element in the unsorted part of the list. Once the smallest element is found, it is swapped with the first element in the unsorted part of the list.

After each pass, the smallest element in the unsorted part of the list will be at the beginning of the unsorted part of the list.

The method continues iterating through the unsorted part of the list until the entire list is sorted.

After the linked list is fully sorted, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.



Constraints:

The linked list can contain duplicates.

The method should be implemented in the LinkedList class.

The method should not use any additional data structures to sort the linked list."""

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

    # WRITE SELECTION_SORT METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def selection_sort(self):
        if self.length < 2:
            return 
        curr = self.head   
        while curr.next is not None:
            smallest = curr
            inner_curr = curr.next
            while inner_curr is not None:
                if inner_curr.value < smallest.value:
                    smallest = inner_curr
                inner_curr = inner_curr.next
            curr.value, smallest.value = smallest.value, curr.value
            curr = curr.next


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(4)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

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

"""    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        while current.next is not None:
            smallest = current
            inner_current = current.next
            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value        
            current = current.next




This code defines a method called selection_sort that is used to sort a linked list in ascending order using the selection sort algorithm. Here is a step-by-step explanation of the code:



The method starts by checking if the length of the linked list is less than 2. If this is the case, the list is already sorted, and the method returns without doing anything.

if self.length < 2:
    return


If the length of the linked list is greater than or equal to 2, the method initializes a variable called current to the head of the list.

current = self.head


The method then enters a while loop that continues until current reaches the second to last node in the list. This is because, on each pass through the loop, the smallest unsorted element is selected and moved to the beginning of the unsorted portion of the list, so we don't need to compare it again on the next pass.

while current.next is not None:


Inside the loop, the method initializes a variable called smallest to the current node and a variable called inner_current to the next node after current.

    smallest = current
    inner_current = current.next


The method then enters an inner while loop that continues until inner_current is None. Inside the loop, the method checks if the value of inner_current is smaller than the value of smallest. If so, the method updates smallest to point to inner_current.

    while inner_current is not None:
        if inner_current.value < smallest.value:
            smallest = inner_current
        inner_current = inner_current.next


After the inner while loop completes, the method checks if smallest is different from the current node. If so, the method swaps their values using Python's tuple unpacking syntax.

    if smallest != current:
        current.value, smallest.value = smallest.value, current.value


Finally, the method moves the current pointer to the next node in the list.

    current = current.next


The linked list is now sorted in ascending order. Note that this implementation modifies the linked list in place and does not return a new list.





Code with inline comments:



# Define a method to sort a linked list in ascending order 
# using the selection sort algorithm
def selection_sort(self):
    # If the linked list has less than 2 elements, it is already sorted
    if self.length < 2:
        return
 
    # Start with the first node as the current node
    current = self.head
 
    # While there is at least one more node after the current node
    while current.next is not None:
        # Assume the current node has the smallest value so far
        smallest = current
        # Start with the next node as the inner current node
        inner_current = current.next
        
        # Find the node with the smallest value among the remaining nodes
        while inner_current is not None:
            if inner_current.value < smallest.value:
                smallest = inner_current
            inner_current = inner_current.next
        
        # If the node with the smallest value is not the current node,
        # swap their values
        if smallest != current:
            current.value, smallest.value = smallest.value, current.value        
 
        # Move to the next node
        current = current.next"""
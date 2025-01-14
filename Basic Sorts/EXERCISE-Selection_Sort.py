"""
Selection Sort
Write a function called selection_sort that sorts a list of integers in ascending order using the Selection Sort algorithm.

The function should perform the following tasks:

Accept a parameter my_list that represents the list of integers to be sorted.

Iterate through the list from the first element to the second-to-last element. For each element i, perform the following steps:

Set min_index to the index of the current element i.

Iterate through the list from the element at position i + 1 to the last element. For each element j, perform the following steps:

Compare the element at position j with the element at position min_index. If the element at position j is less than the element at position min_index, update min_index to the index j.

If the index i is not equal to min_index, swap the elements at positions i and min_index.

Return the sorted list.


"""


## WRITE SELECTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp  
    return my_list




print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

"""The algorithm works by finding the smallest element in the unsorted part of the list and moving it to the beginning of the unsorted part. This process repeats until the entire list is sorted.

Here is how the code works:

The function takes an input list as an argument.

The outer loop of the code runs from 0 to len(my_list) - 2 using the range function. This outer loop will make n-1 passes through the list where n is the length of the list. Each pass will ensure that the smallest element in the remaining unsorted part of the list is moved to the beginning.

The variable min_index keeps track of the index of the smallest element in the unsorted part of the list. It starts at the current index i of the outer loop.

The inner loop runs over each element of the unsorted part of the list, starting from i+1 and running up to the end of the list. It compares each element to the current minimum element and updates min_index if it finds a smaller element. After this loop completes, the smallest element in the unsorted part of the list is found.

If the index of the minimum element is not i, then it swaps the elements at indices i and min_index using a temporary variable called temp. This moves the smallest element to the beginning of the unsorted part of the list.

After the outer and inner loops have run, the sorted list is returned.

Overall, this code sorts a list in ascending order by finding the smallest element in the unsorted part of the list and moving it to the beginning. This process repeats until the entire list is sorted. The time complexity of this algorithm is also O(n^2).





Code with inline comments:



def selection_sort(my_list):
    # loop over the list n-1 times, where n is the length of the list
    for i in range(len(my_list)-1):
        # set the current index as the index of the smallest element
        min_index = i
        # loop over each element in the unsorted part of the list
        for j in range(i+1, len(my_list)):
            # if the current element is smaller than the current minimum, update the minimum index
            if my_list[j] < my_list[min_index]:
                min_index = j
        # if the index of the minimum element is not i, swap the elements at indices i and min_index
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    # return the sorted list
    return my_list
"""
# HT: Item In Common ( ** Interview Question)
# Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

# Use a dictionary to solve the problem that creates an O(n) time complexity.

def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def item_in_common_efficient(list1, list2):
    dict = {}
    for i in list1:
        dict[i] = True
    for j in list2:
        if j in dict:
            return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]

print(item_in_common_efficient(list1, list2))

# def item_in_common(list1, list2):
#     # create an empty dictionary to store list1's values
#     my_dict = {}
 
#     # iterate through list1 and add each value to the dictionary as a key
#     for i in list1:
#         my_dict[i] = True
 
#     # iterate through list2 and check if each value is a key in the dictionary
#     for j in list2:
#         # if a value in list2 is also in the dictionary, return True
#         if j in my_dict:
#             return True
 
#     # if no values in common are found, return False
#     return False
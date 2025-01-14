# Set: Longest Consecutive Sequence ( ** Interview Question)
# Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

# Use sets to optimize the runtime of your solution.

# Input: An unsorted array of integers, nums.

# Output: An integer representing the length of the longest consecutive sequence in nums.

# Example:



# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence in the input array is [4, 3, 2, 1], and its length is 4.

# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################
# def longest_consecutive_sequence(nums):
#     sorted_set = sorted(set(nums))
#     length = 1
#     if sorted_set is None:
#         return 0
#     for i, num in enumerate(sorted_set):
#         if num == sorted_set[i-1] + 1:
#             length += 1
#     return length

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
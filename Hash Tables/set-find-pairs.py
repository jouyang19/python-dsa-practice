# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
# Code Explanation
# Let me explain why we use complement = target - num through an example.
# The goal of this function is to find pairs of numbers (one from each array) that sum up to the target value. In other words, we're looking for numbers x from arr1 and y from arr2 where:
# x + y = target
# When we're looking at a specific number num from arr2 (which represents y in our equation), we need to find what number x from arr1 would make this equation true. We can rearrange the equation:
#  x + y = target
#  x = target - y
# In the code, num represents y, so complement (which represents x) must be target - num.
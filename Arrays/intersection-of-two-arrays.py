"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List
# my solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freq1 = {}
        freq2 = {}
        intersections = []
        
        for num1 in nums1:
            freq1[num1] = freq1.get(num1, 0) + 1
            
        for num2 in nums2:
            freq2[num2] = freq2.get(num2, 0) + 1
            
        for key1 in freq1:
            if key1 in freq2:
                count = min(freq1[key1], freq2[key1])
                intersections.extend([key1] * count)
                    
        return intersections
    
    
"""
2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
If nums1 is small compared to nums2, a better approach is to use a frequency dictionary for the smaller array and iterate over the larger array.

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):  # Ensure nums1 is the smaller array
            nums1, nums2 = nums2, nums1
        
        freq = {}
        result = []
        
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        
        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1
        
        return result


"""
What if the given array is already sorted? How would you optimize your algorithm?
If the arrays are sorted, we can avoid using frequency dictionaries and use two pointers to find the intersection.

Two Pointers Approach:
Use two pointers (i and j) to traverse nums1 and nums2.
Compare the current elements pointed to by i and j:
If nums1[i] == nums2[j], add the element to the result and increment both pointers.
If nums1[i] < nums2[j], increment i.
If nums1[i] > nums2[j], increment j.
Continue until one of the pointers goes out of bounds.

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # Sort if not already sorted
        nums2.sort()
        
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return result
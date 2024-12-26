"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters."""

# Solution using a list  

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) > 10**5 or len(s) < 1:
            return -1
        unique = []
        for char in s:
            if char in unique:
                unique.remove(char)
            else:
                unique.append(char)
        for char in unique:
            if s.count(char) == 1:
                return s.index(char)
        return -1
        
        
# Better solution using a frequency dictionary and enumerate

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) > 10**5 or len(s) < 1: # input limit length; 
            return -1
        
        freq = {}
        
        for char in s:
            freq[char] = freq.get(char, 0) + 1 # the 0 is the default value in case the value char doesn't exist
            
        for i, char in enumerate(s): # enumerate s since the indices are more acurrate in the original string than the freq dict
            if freq[char] == 1: # if there is only one count of a letter appearing, than return the index of the char in s.
                return i
            
        return -1 
    
        


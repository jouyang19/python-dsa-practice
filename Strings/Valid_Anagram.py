"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}
        
        for s_char, t_char in zip(s , t):
            freq_s[s_char] = freq_s.get(s_char, 0) + 1
            freq_t[t_char] = freq_t.get(t_char, 0) + 1
        
        for char in s:
            if char not in t:
                return False
            elif freq_s[char] != freq_t[char]:
                return False
            
        return True
    
"""
Same solution, but shorter:
Time O (2n)
Space On^2
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}
        
        for s_char, t_char in zip(s , t):
            freq_s[s_char] = freq_s.get(s_char, 0) + 1
            freq_t[t_char] = freq_t.get(t_char, 0) + 1
    
            
        return freq_s == freq_t
    
"""
Alternative solution 1 using sorted()
Big O time: O n log (n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        return sorted(t) == sorted(s)
    
"""
Alternative solution 2 using a one dictionary (hashmap) approach and a generator function
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        freq = {}
        
        # Count frequencies of characters in both strings
        for s_char, t_char in zip(s, t):
            freq[s_char] = freq.get(s_char, 0) + 1
            freq[t_char] = freq.get(t_char, 0) - 1
        
        # After processing, all values in freq should be 0 if they are anagrams
        for count in freq.values():
            if count != 0:
                return False
        return True
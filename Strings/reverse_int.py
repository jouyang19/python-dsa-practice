class Solution: # one pointer with range() loop solution
    def reverse(self, x: int) -> int:
        
        is_negative = x < 0
        s = list(str(abs(x)))
        reverse_index = len(s) - 1
        
        for i in range(len(s) // 2):
            s[i], s[reverse_index] = s[reverse_index], s[i]
            reverse_index -= 1
                
        reversed_x = int(''.join(s))
        
        if is_negative:
            reversed_x = -reversed_x
            
        if reversed_x >= 2**31 - 1 or reversed_x <= -2**31:
            return 0
        
        return reversed_x
    
#  Another Solution, two pointers
# reversed_x >= 2**31 - 1 or reversed_x <= -2**31 Problem was asking us to assume that we are working with 32 bit integers

class Solution:
    def reverse(self, x: int) -> int:
        
        is_negative = x < 0
        s = list(str(abs(x)))
        right = len(s) - 1
        left = 0
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
                
        reversed_x = int(''.join(s))
        
        if is_negative:
            reversed_x = -reversed_x
            
        if reversed_x >= 2**31 - 1 or reversed_x <= -2**31:
            return 0
        
        return reversed_x
            
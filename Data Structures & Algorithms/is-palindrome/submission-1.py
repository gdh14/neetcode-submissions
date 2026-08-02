""" 
1. clean string, only keep alphametics
2. two pointer, scan from left and right, if not the same, return False

space O(n)
time O(n)

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''
        for c in s:
            if c.isalpha():
                clean_s += c.lower()    
        
        if len(clean_s) == 0:
            return True
        
        left, right = 0, len(clean_s) - 1

        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        
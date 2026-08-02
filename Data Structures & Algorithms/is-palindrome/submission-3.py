""" 
No clean string solution

two pointer, scan from left and right, skip non alnum with for loop, if not the same, return False

space O(1)
time O(n)


!
l
r

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:        
        left, right = 0, len(s) - 1

        while left <= right:
            # skip non alpha num
            while not s[left].isalnum() and left <= len(s) - 1:
                left += 1
            while not s[right].isalnum() and right >= 0:
                right -= 1

            if left > right:
                break

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        
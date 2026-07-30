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
            while left <= len(s) - 1 and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1

            if left > right:
                break

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        
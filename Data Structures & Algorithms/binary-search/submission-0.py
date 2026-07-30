""" 


t = 6

1 3 5 6
    

l=2
r=3
m=2

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2 

        while l <= r:
            if target > nums[m]:
                l = m + 1
                m = (l + r) // 2
            elif target < nums[m]:
                r = m - 1
                m = (l + r) // 2
            else:
                return m
        
        return -1
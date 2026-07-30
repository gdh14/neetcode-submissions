""" 

1. use dict as counter
- key is each number
- value is the count
- when one value is > 1, return True
- time O(N), space O(N)

2. use set directly (better)
[1,2,3,1]
{1,2,3,}
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        return False

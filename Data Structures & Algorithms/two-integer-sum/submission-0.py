""" 

tgt = 7
nums = [1,3,4]
d = {
    6: 0,
    4: 1,

}

x = 4
key = 3

[1, 2]

key = 7 - 1 = 6
val = idx[x]
d[6] = 0

key = tgt - x
val = idx[x]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            key = target - x
            if x in d:
                return [d[x], i]
            d[key] = i

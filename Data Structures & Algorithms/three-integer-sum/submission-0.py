""" 

nums = [1,0,-1,2,-2]
sorted_nums = [-2, -1, 0, 1, 2, 3]

twoSumSorted(sorted_list, tgt) -> List[List[]]

-2: [[0, 2], [-1, 3]] 
-1: []
0
1
2
3

[1,2,3]

3
0

time complexity O(N2*logN)

return = [[1,0,-1], [0,2-2]]


sorted_nums = [-2, -1, 0, 1]
i = 0
twoSumSorted([-1,0,1], 2) -> []
i = 1
twoSumSorted([0,1], 1) -> [0,1]
res = [[-1, 0, 1]]
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSumSorted(sorted_list: List[int], target: int) -> List[List[int]]:
            res = []
            l, r = 0, len(sorted_list) - 1
            while l < r:
                if sorted_list[l] + sorted_list[r] > target:
                    r -= 1
                elif sorted_list[l] + sorted_list[r] < target:
                    l += 1
                else:
                    res.append([sorted_list[l], sorted_list[r]])
                    r -= 1
                    l += 1
            return res
        
        sorted_nums = sorted(nums)
        res = []
        cur = None
        for i, num in enumerate(sorted_nums):
            if i > len(sorted_nums) - 3:
                break
            if num == cur:
                continue
            cur = num
            two_ele_list = twoSumSorted(sorted_nums[i + 1:], -num)
            if len(two_ele_list) > 0:
                for a, b in two_ele_list:
                    res.append([num, a, b])
        
        return res

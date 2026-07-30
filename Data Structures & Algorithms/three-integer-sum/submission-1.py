"""
                                 l2,r   
nums = [-2, -2, -1, 0, 1, 1, 2, 2]
                             l1 

[-2, 0, 2]
[-2, 0, 2]




"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort num
        nums.sort()

        # iterate 
        for l1 in range(len(nums)):
            # skip duplicate of l1
            if l1 > 0 and nums[l1] == nums[l1 - 1]:
                continue

            l2 = l1 + 1
            r = len(nums) - 1
            while l2 < r:
                if nums[l1] + nums[l2] + nums[r] > 0:
                    r -= 1
                elif nums[l1] + nums[l2] + nums[r] < 0:
                    l2 += 1
                else:
                    res.append([nums[l1], nums[l2], nums[r]])
                    l2 += 1
                    r -= 1
                    while nums[l2] == nums[l2 - 1] and l2 < r:
                        l2 += 1
                    while nums[r] == nums[r + 1] and r > l2:
                        r -= 1
        
        return res



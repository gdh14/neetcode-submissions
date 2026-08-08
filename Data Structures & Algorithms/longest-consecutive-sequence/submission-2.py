""" 
Usage of Hashset.

Step
1. locate all potential starting number: num - 1 must not in nums
2. for each starting number, increment by one until not in hashset, maintain max

Example: 
nums = [1,1,2,4,5,6]
nums_set = set([1,2,4,5,6])
start_nums = [1,4]

max_len = 2

start_num = 4
temp_len = 3
num = 7

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        start_nums = []
        for num in nums_set:
            if num - 1 not in nums_set:
                start_nums.append(num)
        
        max_len = 0
        for start_num in start_nums:
            temp_len = 0
            num = start_num 
            while num in nums_set:
                temp_len += 1
                num += 1
            max_len = max(max_len, temp_len)
        
        return max_len

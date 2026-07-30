""" 
Bucket Sort O(N)

maintain a freq list with length len(nums) + 1. 
Each index store a list of num with that freq. 

freq = [[], [], [1,2], [4]]

k = 3

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in counter.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) > 0:
                res.extend(freq[i])
                if len(res) == k:
                    return res



        
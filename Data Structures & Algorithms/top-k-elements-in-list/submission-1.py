"""
Simple O(NlogN)

k=2
[1,2,2,3,3,3,3]

3
2

counter = {
    1: 1,
    2: 2,
    3: 4
}

1. counter
space O(n)
time O(n)

2. sorting
space O(n) 
time O(nlogn)


k = 2
nums = [1,1,2,2,3]
res = [1, 2]

counter = {
    1: 2,
    2: 2,
    3: 1
}

sorted_kv_pairs = [(1,2), (2,2), (3,1)]

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # sort values
        sorted_kv_pairs = sorted([(k, v) for k, v in counter.items()], 
            key=lambda x: -x[1])


        res = []
        for i in range(k):
            res.append(sorted_kv_pairs[i][0])

        return res
 
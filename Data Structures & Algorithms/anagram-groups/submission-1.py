""" 
Solution 2: Use 26 char counter as key

O(N * L)

"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            # convert list to tuple to formulate key
            group[tuple(count)].append(s)
        
        return list(group.values())
        
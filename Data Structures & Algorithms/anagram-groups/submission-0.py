""" 
Solution 1: Sort each string

O(N * L * log(L))

"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            # remember to join the back
            sorted_s = ''.join(sorted(s))
            group[sorted_s].append(s)
        
        return list(group.values())
        
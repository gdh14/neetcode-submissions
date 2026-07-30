"""
1. use dict.
- s / t anagram <-> counter(s) == counter(t)
- time: O(n+m)
- space: O(n+m)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = {}, {}

        # count char in s
        for char_s in s:
            if char_s in s_counter: 
                s_counter[char_s] += 1
            else:
                s_counter[char_s] = 1
        
        # count char in t
        for char_t in t:
            if char_t in t_counter: 
                t_counter[char_t] += 1
            else:
                t_counter[char_t] = 1
        
        return s_counter == t_counter
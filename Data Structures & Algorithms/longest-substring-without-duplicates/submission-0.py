
""" 
Sliding window. personal try with neetbot hint.

important thing is to understand we should increment l until s[r] is not in the set.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, len(char_set))
        
        return max_len


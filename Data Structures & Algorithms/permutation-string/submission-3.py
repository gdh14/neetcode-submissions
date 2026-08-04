"""
Neetcode standard solution, sliding window, 

substring match <=> frequency array of the fixed size string is matching for all 26 letters.

Algorithm:

- set fixed window of s2, with same lenght as s1
- initialize freq array, a1 and a2 (I will use dict to represent)
- maintain match variable
- slide the fixed window in s2, update a2 and match accordingly
    - return True when match == 26

Example: 
s1 = abc
s2 = laacbe
      l
        r 
a1: 
- a: 1
- b: 1
- c: 1
- l: 0

a2:
- a: 2
- b: 0
- c: 1 -> 0
- l: 1

match = 22

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case when s1 is too long
        if len(s1) > len(s2):
            return False

        # intialize frequency array for s1 and s2-sub
        a1 = [0] * 26
        a2 = [0] * 26
        for c in s1:
            a1[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            a2[ord(c) - ord('a')] += 1

        # count total freq match
        match = 0
        for i in range(len(a1)):
            if a1[i] == a2[i]:
                match += 1
        
        # return True directly, maybe redundant
        if match == 26: return True

        # iterate fixed sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            # --- add to window: update freq array of s2-sub, update match ---
            index = ord(s2[r]) - ord('a')
            a2[index] += 1
            # add a new match
            if a2[index] == a1[index]:
                match += 1
            # used to be match, now adding to the value will decrease a match count
            elif a2[index] == a1[index] + 1:
                match -= 1
            # else, match no change
                
            # --- remove from window ---
            index = ord(s2[l]) - ord('a')
            a2[index] -= 1
            if a2[index] == a1[index]:
                match += 1
            elif a2[index] == a1[index] - 1:
                match -= 1
            l += 1
            
            if match == 26:
                return True

        return False

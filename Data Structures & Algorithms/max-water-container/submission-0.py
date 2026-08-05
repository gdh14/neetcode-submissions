""" 
Two pointer, but a bit tricky to think. see intuition below

# core equation to calculate area
area = min(h[l], h[r]) * (r - l)

# how two pointer work (intuition)
- We start with the widest container (left at start, right at end).
- The height is limited by the shorter line, so to potentially increase the area, we must move the pointer at the shorter line inward.
Moving the taller line never helps because it keeps the height the same but reduces the width. (Here is the pruning: the O(N2) method will include moving the taller line, but moving the taller line will have no bigger array than current state, so should be pruned)
- By always moving the shorter side, we explore all meaningful possibilities.

# example
1,6,5,4
  l
  r

"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = min(heights[l], heights[r]) * (r - l)

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, min(heights[l], heights[r]) * (r - l))
        
        return max_area
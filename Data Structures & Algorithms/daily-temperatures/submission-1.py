"""
Monotonic Stack Foundation, a must-revisit classic problem!

temp = [2,3,3,1,5,9,3]

i = 1
t = 3

(1,3)

stack = [9,
res = []
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        # maintain non-increasing stack
        for i, t in enumerate(temperatures):
            # pop if the incoming value is large
            while len(stack) > 0 and stack[-1][1] < t:
                stack_i, stack_t = stack.pop()
                res[stack_i] = i - stack_i
            # push new value
            stack.append((i, t))
        
        return res

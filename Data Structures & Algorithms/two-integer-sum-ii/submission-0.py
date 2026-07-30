"""

num = [1,2,3,6]
       l
             r
target = 4

num = [1,2]
       l r
target = 3


while l < r:
num[l] + num[r] > target -> r -= 1
num[l] + num[r] < target -> l -= 1
num[l] + num[r] == target -> return l+1 r+1

output (1-indexed) -> [1,3]

num = [1,2,3]
t = 3
l = 0
r = 1
sum = 3

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                return [l + 1, r + 1]
                
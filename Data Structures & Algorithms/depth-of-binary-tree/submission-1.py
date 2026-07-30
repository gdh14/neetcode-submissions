# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS solution.

Obtain the level with BFS by maintaining a queue.

Test:

1
2   3
4 5

q=[2,3] level=1
q=[4,5] level=2
q=[] level=3


"""
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        level = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

            
            
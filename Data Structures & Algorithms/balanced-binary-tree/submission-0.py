# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 

check each node's left and right's height, 
maintain global variable self.is_balanced = True


left_h
right_h

if abs(left_h - right_h) > 1:
    self.is_balanced = False    

"""

import math

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def dfs(node):
            if node is None:
                return 0
            
            # get left and right height
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # check if height-balanced
            if abs(left_h - right_h) > 1:
                self.is_balanced = False
            
            return max(left_h, right_h) + 1
        
        dfs(root)

        return self.is_balanced











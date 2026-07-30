# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 
Bottom-up Idea
- for each node, we first get inverted left and right sub-tree
- and then swap left and right to current node

This is a post-order traversal + decompose problem into subproblems
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None

        # get inverted left and right
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        # for current node, swap left and right to get inverted tree for CURRENT node
        root.left, root.right = right_inverted, left_inverted

        return root
        
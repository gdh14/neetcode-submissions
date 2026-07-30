# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 
Top Down Idea

What invertTree() does:
- for each node, swap its children
- for each of its children, call invertTree() (to swap it's children)

This is a pre-order traversal. swap first, and then traverse
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return None
        
        # swap left and right child
        root.left, root.right = root.right, root.left

        # recursively run invertTree top-down
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
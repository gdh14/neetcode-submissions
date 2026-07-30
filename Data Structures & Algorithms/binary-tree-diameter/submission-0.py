# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # return the height 
        def dfs(node):
            if node is None:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # update diameter
            self.res = max(self.res, left_h + right_h)

            return 1 + max(left_h, right_h)

        # need to execute dfs!!
        dfs(root)

        return self.res
        
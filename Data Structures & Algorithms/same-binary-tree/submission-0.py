# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


""" 

1
2 3


1
2. 3
   4. 5
""" 

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        # check value same
        if p.val != q.val:
            return False

        # check children same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
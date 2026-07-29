# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fn(root):
            if root == None:
                return 0
            lh = fn(root.left) 
            rh = fn(root.right)
            return 1 + max(lh, rh)
        return fn(root)
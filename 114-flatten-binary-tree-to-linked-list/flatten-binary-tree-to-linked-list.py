# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def fn(root):
            if root == None:
                return
            nonlocal prev
            fn(root.right)
            fn(root.left)
            root.left = None
            root.right = prev
            prev = root
        return fn(root)
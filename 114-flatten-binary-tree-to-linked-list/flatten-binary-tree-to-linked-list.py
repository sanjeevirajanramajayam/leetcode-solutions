# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        def fn(root):
            nonlocal prev
            if root == None:
                return None 
            fn(root.right)
            fn(root.left)
            root.left = None 
            root.right = prev 
            prev = root 
        fn(root)
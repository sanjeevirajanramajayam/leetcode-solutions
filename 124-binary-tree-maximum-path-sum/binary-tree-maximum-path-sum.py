# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def fn(root):
            nonlocal maxi
            if root == None:
                return 0

            left = max(0, fn(root.left))
            right = max(0, fn(root.right))
            maxi = max(maxi, root.val + left+ right)
            return root.val + max(left, right)
        fn(root)
        return maxi
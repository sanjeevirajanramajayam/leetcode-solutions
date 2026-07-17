# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float(
            '-inf'
        )
        def fn(root):
            nonlocal ans
            if not root:
                return 0

            lh = fn(root.left)
            rh = fn(root.right)

            lh = max(lh, 0)
            rh = max(rh, 0)
            
            ans = max(ans, lh + rh + root.val)

            return root.val + max(lh, rh)
        fn(root)
        return ans
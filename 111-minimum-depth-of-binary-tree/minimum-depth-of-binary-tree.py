# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def preorder(root):
            if root == None:
                return 0
            left = float('inf')
            right = float('inf')
            if root.left:
                left = preorder(root.left)
            if root.right:
                right = preorder(root.right)
            if not root.left and not root.right:
                return 1

            return 1 + min(left, right)
        
        return preorder(root)
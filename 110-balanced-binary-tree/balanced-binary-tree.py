# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if root == None:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)

            if left is False or right is False:
                return False

            if abs(left - right) > 1:
                return False
            
            return 1 + max(left, right)
        x = traverse(root)
        if x is False:
            return x
        else:
            return True
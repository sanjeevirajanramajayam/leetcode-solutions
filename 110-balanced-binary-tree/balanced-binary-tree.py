# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def preorder(root):
            if root == None:
                return 0
            
            left = preorder(root.left)
            right = preorder(root.right)

            if left is False or right is False:
                return False

            left += 1
            right += 1

            if abs(left - right) > 1:
                return False
            
            return max(left, right)
        return preorder(root) is not False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def inorder(root, currSum):
            nonlocal ans
            if root == None:
                return 0
            if root.left == None and root.right == None:
                ans += currSum * 10 + root.val 
            
            left = inorder(root.left, currSum * 10 + root.val)
            right = inorder(root.right, currSum * 10 + root.val)

        inorder(root, 0) 
        return ans
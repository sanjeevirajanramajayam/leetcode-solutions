# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inorder(root, currSum):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                if currSum + root.val == targetSum:
                    return True
            
            left = inorder(root.left, currSum + root.val)
            right = inorder(root.right, currSum + root.val)

            if left is True:
                return True
            
            if right is True:
                return True
            return False
        if inorder(root, 0) is True:
            return True 
        else: 
            return False
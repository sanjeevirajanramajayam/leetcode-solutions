# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum = 0
        def rev(root):
            nonlocal sum
            if root == None:
                return None
            
            rev(root.right)
            sum += root.val
            root.val = sum
            rev(root.left)
        rev(root)
        return root
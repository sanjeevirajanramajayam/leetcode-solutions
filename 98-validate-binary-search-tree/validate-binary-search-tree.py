# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def isValid(root, minVal, maxVal):
            if root == None:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return isValid(root.right, root.val, maxVal) and isValid(root.left, minVal, root.val)
        
        return isValid(root, float('-inf'), float('inf'))
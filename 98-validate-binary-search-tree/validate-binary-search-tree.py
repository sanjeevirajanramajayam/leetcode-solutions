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
        def v(root, l, r):
            if not root:
                return True

            if root.val <= l or root.val >= r:
                return False
            
            return v(root.left, l, root.val) and v(root.right, root.val, r)
        return v(root, float('-inf'), float('inf'))
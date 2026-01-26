# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def maxH(root):
            if root == None:
                return 0
            
            left = maxH(root.left)
            right = maxH(root.right)
        
            return max(left, right) + 1

        return maxH(root)
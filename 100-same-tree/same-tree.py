# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def isSameTree(r1, r2):
            if (r1 == None and r2 is not None) or (r2 == None and r1 is not None):
                return False
            
            if r1 == None and r2 == None:
                return True
            
            return r1.val == r2.val and isSameTree(r1.left, r2.left) and isSameTree(r1.right, r2.right)
        
        return isSameTree(p, q)
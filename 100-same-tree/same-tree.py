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
        
        def isSame(p, q):
            if p == None or q == None:
                return (p == q)
            
            return isSame(p.left, q.left) and isSame(p.right, q.right) and p.val == q.val
        return isSame(p, q)
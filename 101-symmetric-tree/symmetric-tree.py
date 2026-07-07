# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(p, q):
            if p == None or q == None:
                return p == q
            return p.val == q.val and isSame(p.left, q.right) and isSame(p.right, q.left)
        return isSame(root.left, root.right)
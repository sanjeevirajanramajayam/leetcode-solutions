# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0]
        def maxH(root):
            if root == None:
                return 0
            
            lh = maxH(root.left)
            rh = maxH(root.right)

            res[0] = max(res[0], lh + rh)

            return 1 + max(lh, rh)
        maxH(root)
        return res[0]
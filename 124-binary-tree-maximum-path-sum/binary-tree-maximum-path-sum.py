# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [float('-inf')]
        def maxH(root):
            if root == None:
                return 0
            
            lh = max(0, maxH(root.left))
            rh = max(0, maxH(root.right))

            res[0] = max(res[0], root.val + lh + rh)

            return root.val + max(lh, rh)

        maxH(root)
        return res[0]
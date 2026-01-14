# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def maxH(root):
            if root == None:
                return 0

            lh = maxH(root.left)
            rh = maxH(root.right)

            if lh == -1 or rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1

            return 1 + max(lh, rh)
        return maxH(root) != -1
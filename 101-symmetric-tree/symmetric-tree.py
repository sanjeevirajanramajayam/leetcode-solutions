# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if p == None or q == None:
                return p == q
            # print(p.val, q.val)
            return p.val == q.val and isSame(p.left, q.right) and isSame(p.right, q.left)
        return isSame(root.left, root.right)
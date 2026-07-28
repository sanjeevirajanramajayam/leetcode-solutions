# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, left, right):
            if not root:
                return True
            # print(root.val, left, right, left <= root.val, root.val <= right)
            if not (left < root.val < right):
                return False
            if not valid(root.left, left, root.val):
                return False
            if not valid(root.right, root.val, right):
                return False
            return True
        return valid(root, float('-inf'), float('inf'))

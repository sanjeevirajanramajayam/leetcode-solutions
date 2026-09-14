# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def isOne(root):
            if not root:
                return None
            if root.val == 1:
                return True
            if isOne(root.left) is True:
                return True
            if isOne(root.right) is True:
                return True
            return None
        def fn(root):
            if not root:
                return None
            # print(root, isOne(root))
            # return None
            if isOne(root) is None:
                return None
            # print(root, isOne(root))
            if isOne(root.left) is True:
                fn(root.left)
            else:
                root.left = None
            if isOne(root.right) is True:
                fn(root.right)
            else:
                root.right = None
            # root.right = isOne(root.right)
            return root
        return fn(root)
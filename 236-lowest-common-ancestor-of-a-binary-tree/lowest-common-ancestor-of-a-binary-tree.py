# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fn(root):
            if (root == None):
                return None
            lh = fn(root.left)
            rh = fn(root.right)
            # print(lh, rh, root.val)
            if root.val == p.val:
                return root
            
            if root.val == q.val:
                return root

            if lh and rh:
                return root

            if lh and not rh:
                return lh

            if rh and not lh:
                return rh


        return fn(root)

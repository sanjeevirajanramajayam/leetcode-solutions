# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def fn(root, lb, rb):
            target = root.val
            if p.val < target and q.val < target:
                return fn(root.left, lb, root.val)
            elif p.val > target and q.val > target:
                return fn(root.right, root.val, rb)
            else:
                return root
        return fn(root, float('-inf'), float('inf'))
            

            
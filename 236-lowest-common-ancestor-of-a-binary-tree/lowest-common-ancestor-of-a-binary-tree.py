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
        def fn(root):
            if root == None:
                return None

            if root.val == p.val:
                return root
            
            if root.val == q.val:
                return root

            left = fn(root.left)
            right = fn(root.right)

            if left != None and right != None:
                return root

            if left != None:
                return left
            
            if right != None:
                return right
        return fn(root)

            



        
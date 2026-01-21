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
        def postOrder(root):
            if root == None:
                return None
            if root.val == p.val:
                return root
            if root.val == q.val:
                return root
            left = postOrder(root.left)
            right = postOrder(root.right)
            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        return postOrder(root)
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

        def preOrderTraversal(node):
            if node == None:
                return None
            
            if node.val == p.val:
                return node
            
            if node.val == q.val:
                return node
            
            lh = preOrderTraversal(node.left)
            rh = preOrderTraversal(node.right)

            if not lh:
                return rh
            
            if not rh:
                return lh
            
            return node
        
        lca = preOrderTraversal(root)
        return lca

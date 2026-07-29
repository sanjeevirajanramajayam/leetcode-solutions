# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fn(node):
            if node == None:
                return None
            # print(node.val, p.val, q.val)
            if node.val > p.val and node.val > q.val:
                if fn(node.left) is not None:
                    return fn(node.left) 
            elif node.val < p.val and node.val < q.val:
                if fn(node.right) is not None:
                    return fn(node.right)
            else:
                # print(node.val)
                return node
        return fn(root)
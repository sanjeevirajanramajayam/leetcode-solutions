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
                return 
            if node.val == p.val:
                return node 
            
            if node.val == q.val:
                return node 
            left = fn(node.left)
            right = fn(node.right)

            if left and right:
                return node 
            
            if left:
                return left 
            
            if right:
                return right 
            

        ans = fn(root)
        if ans:
            return ans
        # return fn(root).val
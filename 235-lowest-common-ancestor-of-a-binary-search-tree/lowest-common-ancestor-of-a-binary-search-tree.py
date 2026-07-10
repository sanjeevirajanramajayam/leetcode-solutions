# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root):
            if root == None:
                return

                
            if root.val == p.val:
                return root
            
            if root.val == q.val:
                return root


            left = lca(root.left)
            right = lca(root.right)
            # print(root.val)
            # if left:
            #     print(left.val)
            # else:
            #     print("None")
            # if right:
            #     print(right.val)
            # else:
            #     print("None")

            if left and right:
                return root

            if left:
                return left
            
            if right:
                return right
        
        return lca(root)
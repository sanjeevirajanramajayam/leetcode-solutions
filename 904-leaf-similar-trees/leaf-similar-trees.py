# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []
        def inorder(root, l):
            if root == None:
                return
            inorder(root.left, l)
            
            if not root.left and not root.right:
                l.append(root.val)
            
            inorder(root.right, l)
        inorder(root1, t1)
        inorder(root2 ,t2)
        # print(t1, t2)
        return t1 == t2



        # adde(t1)
        # print(t1)


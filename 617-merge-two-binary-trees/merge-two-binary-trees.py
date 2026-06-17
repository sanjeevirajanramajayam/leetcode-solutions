# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        def preorder(root1, root2):
            if root1 == None and root2 == None:
                return
            
            root1.val += root2.val

            if root1.left is None and root2.left is not None:
                root1.left = TreeNode(0)
            
            if root1.right is None and root2.right is not None:
                root1.right = TreeNode(0)

            if root2.left:
                preorder(root1.left, root2.left)
            
            if root2.right:
                preorder(root1.right, root2.right)
        
        preorder(root1, root2)
        return root1


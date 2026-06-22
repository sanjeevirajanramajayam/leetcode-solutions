# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            if root1 == None:
                return root1 == root2
            if root2 == None:
                return root1 == root2
            return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def preorder(root):
            if root == None:
                return

            if isSameTree(root, subRoot) is True:
                return True
            
            if preorder(root.left) is True:
                return True
            
            if preorder(root.right) is True:
                return True

            return False
        return preorder(root)
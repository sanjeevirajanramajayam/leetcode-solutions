# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def flattenList(root):
            if root == None:
                return None
            
            flattenList(root.left)
            flattenList(root.right)
            
            rightRoot = root.right
            root.right = root.left
            root.left = None
        
            curr = root

            while curr.right:
                curr = curr.right
            
            curr.right = rightRoot
        
        flattenList(root)
        
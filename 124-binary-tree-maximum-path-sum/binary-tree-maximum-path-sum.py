# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.answer = float('-inf')

        def maxH(root):
            if root == None:
                return 0
            
            lh = max(0, maxH(root.left))
            rh = max(0, maxH(root.right))

            self.answer = max(self.answer, root.val + lh + rh)

            return root.val + max(lh, rh)
    
        maxH(root)
        
        return self.answer 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # Time Complexity : O((log n) ^ 2)
        # Space Complexity: O(1)

        def heightFind(root):
            if root == None:
                return 0
            
            lh = leftHeight(root)
            rh = rightHeight(root)

            if (lh == rh):
                return 2 ** (lh) - 1
            else:
                return 1 + heightFind(root.left) + heightFind(root.right)

        def leftHeight(root):
            hgt = 0
            while root:
                hgt += 1
                root = root.left
            return hgt

        def rightHeight(root):
            hgt = 0
            while root:
                hgt += 1
                root = root.right
            return hgt
        
        return heightFind(root)
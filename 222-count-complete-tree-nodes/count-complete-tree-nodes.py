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
        def heightFind(node):
            if node == None:
                return 0
            
            lh = leftHeight(node)
            rh = rightHeight(node)

            if lh == rh:
                return 2 ** (lh) - 1
            else:
                return heightFind(node.left) + heightFind(node.right) + 1
        
        def leftHeight(node):
            hgt = 0
            while node:
                hgt += 1
                node = node.left
            return hgt
        
        def rightHeight(node):
            hgt = 0
            while node:
                hgt += 1
                node = node.right
            return hgt
        
        return heightFind(root)
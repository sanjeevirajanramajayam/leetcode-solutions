# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.middle = None
        self.last = None

        def inOrder(root):
            if root == None:
                return None
            if root.left:
                inOrder(root.left)
            if self.prev != None and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = root
                else:
                    self.last = root
            self.prev = root
            if root.right:
                inOrder(root.right)

        inOrder(root)

        if self.last:
            temp = self.first.val
            self.first.val = self.last.val
            self.last.val = temp
        else:
            temp = self.first.val
            self.first.val = self.middle.val
            self.middle.val = temp
        
        return root
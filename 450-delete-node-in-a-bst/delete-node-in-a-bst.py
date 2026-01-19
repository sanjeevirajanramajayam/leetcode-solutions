# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None


        def helperFn(root):
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            maxLeft = root.left
            while maxLeft.right:
                maxLeft = maxLeft.right
            
            maxLeft.right = root.right

            return root.left

        dummy = root

        if root.val == key:
            return helperFn(root)
        

        while root != None:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = helperFn(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helperFn(root.right)
                    break
                else:
                    root = root.right

        return dummy

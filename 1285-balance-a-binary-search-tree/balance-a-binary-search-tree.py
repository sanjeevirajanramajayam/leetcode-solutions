# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        inOrder = []
        def inorder(root):
            if root == None:
                return None
            
            inorder(root.left)
            inOrder.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        def reconstruct(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            print(mid, l, mid - 1, mid + 1, r)
            root = TreeNode(inOrder[mid])
            root.left = reconstruct(l, mid - 1)
            root.right = reconstruct(mid + 1, r)
            return root
        
        return reconstruct(0, len(inOrder) - 1)
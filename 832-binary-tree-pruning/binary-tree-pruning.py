# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode | None) -> TreeNode | None:
        def postorder(root):
            if root == None:
                return 
            left = postorder(root.left)
            right = postorder(root.right)
            # print(root.val, left, right)
            if left is None:
                root.left = None 
            if right is None:
                root.right = None 
            if right  or left  or root.val == 1:
                return root 
            elif left is False and right is False:
                return None
        return postorder(root)
         
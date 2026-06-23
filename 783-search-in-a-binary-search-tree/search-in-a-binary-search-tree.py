# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(root):
            if root == None:
                return None
            # print(root.val)
            if root.val == val:
                return root
            
            if val > root.val:
                x = traverse(root.right) 
                if x is not None:
                    return x
            else:
                x = traverse(root.left)
                if x is not None:
                    return x 
        return traverse(root)
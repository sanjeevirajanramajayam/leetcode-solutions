# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        temp = []
        def inorder(root):
            if root == None:
                return None
            inorder(root.left)

            temp.append(root.val)
            inorder(root.right)
        inorder(root1)
        inorder(root2)
        return sorted(temp)
            
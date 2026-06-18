# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def traverse(root):
            # print(root.val)
            # if root.left:
            #     print(root.left.right, root.left.left)
            # if root.right:
            #     print(root.right.left,)
            if root == None:
                return 0

            take = root.val
            templ = float('-inf')
            tempr = float('-inf')
            if root.left:
                templ = max(templ, traverse(root.left.left) + traverse(root.left.right))
            if root.right:
                tempr = max(tempr, traverse(root.right.left) + traverse(root.right.right))
            if templ == float('-inf'):
                templ = 0
            if tempr == float('-inf'):
                tempr = 0
            take += templ
            take += tempr

            not_take = traverse(root.left) + traverse(root.right) 
            left = "None"
            right = "None"
            if root.left:
                left = root.left.val
            if root.right:
                right = root.right.val
            # print(root.val, take, not_take, left, right)
            return max(take, not_take)
        
        return traverse(root)
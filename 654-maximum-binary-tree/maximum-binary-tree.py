# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None

            if left == right:
                return TreeNode(nums[left])
            
            max_ind = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_ind]:
                    max_ind = i
            
            root = TreeNode(nums[max_ind])
            root.left = build(left, max_ind - 1)
            root.right = build(max_ind + 1, right)
            
            return root
        return build(0, len(nums) - 1)
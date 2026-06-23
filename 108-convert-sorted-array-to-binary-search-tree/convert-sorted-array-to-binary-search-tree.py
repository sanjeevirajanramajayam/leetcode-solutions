# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fn(l, r):
            print(l, r)
            if l>r:
                return
            if l == r:
                return TreeNode(nums[l])
            mid = (l + r + 1) // 2
            # print(mid, nums)
            if mid >= len(nums):
                mid -= 1
            root = TreeNode(nums[mid])
            root.left = fn(l, mid - 1)
            root.right = fn(mid + 1, r)
            return root
        return fn(0, len(nums) - 1)
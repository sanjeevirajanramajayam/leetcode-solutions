# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def inorder(root, currSum, arr, ans):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                if currSum + root.val == targetSum:
                    ans.append(arr + [root.val])
            
            left = inorder(root.left, currSum + root.val, arr + [root.val], ans)
            right = inorder(root.right, currSum + root.val, arr + [root.val], ans)

            if left is True:
                return True
            
            if right is True:
                return True
            return False
        inorder(root, 0, [], ans)
        return ans
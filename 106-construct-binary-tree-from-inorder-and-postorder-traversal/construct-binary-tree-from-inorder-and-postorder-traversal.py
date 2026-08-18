# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hash = {}

        for i in range(len(inorder)):
            hash[inorder[i]] = i

        print(hash)

        def fn(inStart, inEnd, postStart, postEnd):
            if (inStart > inEnd or postStart > postEnd):
                return None
            
            root = TreeNode(postorder[postEnd])
            inIdx = hash[postorder[postEnd]]
            rightSize = inEnd - inIdx
            root.left = fn(inStart, inIdx - 1, postStart, postEnd - rightSize - 1)
            root.right = fn(inIdx + 1, inEnd, postEnd - rightSize, postEnd - 1)
            return root
        return fn(0, len(inorder) - 1, 0, len(inorder) - 1)

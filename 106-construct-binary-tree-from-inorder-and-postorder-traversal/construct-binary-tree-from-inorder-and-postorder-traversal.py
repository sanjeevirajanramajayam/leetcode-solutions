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
        
        def build(inStart, inEnd, postStart, postEnd):
            if (inStart > inEnd or postStart > postEnd):
                return
            
            inIdx = hash[postorder[postEnd]]
            rightSize = inEnd - inIdx
            root = TreeNode(postorder[postEnd])
            root.left = build(inStart, inIdx - 1, postStart, postEnd - rightSize - 1)
            root.right = build(inIdx + 1, inEnd, postStart - rightSize, postEnd - 1)
            return root
        n = len(inorder)
        return build(0, n - 1, 0, n - 1)

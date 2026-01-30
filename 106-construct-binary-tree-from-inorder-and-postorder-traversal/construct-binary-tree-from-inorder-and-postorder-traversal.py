# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def buildRoot(inStart, inEnd, postStart, postEnd, inMap):
            if inStart > inEnd or postStart > postEnd:
                return None
            
            root = TreeNode(postorder[postEnd])

            inRoot = inMap[postorder[postEnd]]
            numsRight = inEnd - inRoot 

            root.right = buildRoot(inRoot + 1, inEnd,postEnd - numsRight,  postEnd - 1, inMap)
            root.left = buildRoot(inStart, inRoot -1,postStart, postEnd - numsRight - 1, inMap)

            return root

        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        return buildRoot(0, len(inorder) - 1, 0, len(postorder) - 1, inMap)
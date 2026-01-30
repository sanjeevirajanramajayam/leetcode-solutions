# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        def buildRoot(inStart, inEnd, preStart, preEnd, inMap):
            if inStart > inEnd or preStart > preEnd:
                return None
            
            root = TreeNode(preorder[preStart])

            inRoot = inMap[preorder[preStart]]
            numsLeft = inRoot - inStart

            root.left = buildRoot(inStart, inRoot - 1, preStart + 1, preStart + numsLeft, inMap)
            root.right = buildRoot(inRoot + 1, inEnd, preStart + numsLeft + 1, preEnd, inMap)

            return root

        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        
        node = buildRoot(0, len(inorder) - 1, 0, len(preorder) - 1, inMap)
        return node
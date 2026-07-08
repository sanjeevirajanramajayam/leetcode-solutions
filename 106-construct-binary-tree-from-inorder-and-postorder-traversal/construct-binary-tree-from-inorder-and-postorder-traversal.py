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
        
        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i  
        
        def fn(ins, ends, ps, pe):
            if (ins > ends or ps > pe):
                return
            
            root = TreeNode(postorder[pe])
            inIdx = hashmap[postorder[pe]]
            rightSize = ends - inIdx
            root.left = fn(ins, inIdx - 1, ps, pe - rightSize - 1)
            root.right = fn(inIdx + 1, ends, pe - rightSize, pe - 1)
            return root

        return fn(0, len(inorder) - 1, 0, len(inorder) - 1)



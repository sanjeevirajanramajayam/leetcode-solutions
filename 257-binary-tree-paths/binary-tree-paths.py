# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []

        def preOrder(root, path):
            if root == None:
                return

            if not root.left and not root.right:
                newArr = path[:] + [str(root.val)]
                ans.append("->".join(newArr))
            
            path.append(str(root.val))

            preOrder(root.left, path)
            preOrder(root.right, path)

            path.pop()
        
        preOrder(root, [])
        return ans
            
            
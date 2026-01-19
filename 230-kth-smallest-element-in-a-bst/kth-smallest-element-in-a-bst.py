# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = [0, -1]
        def inOrder(node):
            if node == None:
                return None
            inOrder(node.left)
            count[0] += 1
            # print(count[0])
            if count[0] == k:
                count[1] = node.val
            inOrder(node.right)
        inOrder(root)
        return count[1]

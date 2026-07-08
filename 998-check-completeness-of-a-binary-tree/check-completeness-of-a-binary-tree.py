# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node == None:
                break
            queue.append(node.left)
            queue.append(node.right)
        for i in queue:
            if i != None:
                return False
        return True
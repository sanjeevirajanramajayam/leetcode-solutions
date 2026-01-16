# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        queue = deque([(root, 0)])
        maxWidth = 0
        while queue:
            size = len(queue)
            first = -1
            last = -1
            for i in range(size):
                node, id = queue.popleft()
                if i == 0:
                    first = id
                if i == size - 1:
                    last = id
                if node.left:
                    queue.append((node.left, 2 * id + 1))
                if node.right:
                    queue.append((node.right, 2 * id + 2))
            maxWidth = max(maxWidth, last - first + 1)
        return maxWidth


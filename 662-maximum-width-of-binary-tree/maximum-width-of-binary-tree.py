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
            min_val = -1
            for i in range(size):
                root, ind = queue.popleft()
                if i == 0:
                    first = ind
                
                if i == size - 1:
                    last = ind

                if root.left:
                    queue.append((root.left, (ind - first) * 2 + 1))

                if root.right:
                    queue.append((root.right, (ind - first) * 2 + 2))
            
            maxWidth = max(maxWidth, (last - first + 1))

        return maxWidth
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if root == None:
            return None

        nodeList = []

        def levelOrder(root):
            queue = [(root, 0, 0)]
            while queue:
                size = len(queue)
                for i in range(size):
                    root, row, col = queue.pop()
                    nodeList.append((root.val, row, col))
                    if root.left:
                        queue.append((root.left, row + 1, col - 1))
                    if root.right:
                        queue.append((root.right, row + 1, col + 1))
        levelOrder(root)
        nodeList = sorted(nodeList, key = lambda x: (x[2], x[1], x[0]))
        prevCol = float('inf')
        res = []
        for i in nodeList:
            if i[2] != prevCol:
                res.append([])
                prevCol = i[2]
            res[-1].append(i[0])
        return res

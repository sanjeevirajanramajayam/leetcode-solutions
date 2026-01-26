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
            return []
        
        nodeList = []

        def levelOrder(root):
            queue = deque([(root, 0, 0)])
            while queue:
                size = len(queue)
                for i in range(size):
                    node, row, col = queue.popleft()
                    nodeList.append((node.val, row, col))
                    if node.left:
                        queue.append((node.left, row + 1, col - 1))
                    if node.right:
                        queue.append((node.right, row + 1, col + 1))
        levelOrder(root)
        nodeList = sorted(nodeList, key= lambda x: (x[2], x[1], x[0]))
        ans = []
        prevCol = float('inf')
        for i in range(len(nodeList)):
            if prevCol != nodeList[i][2]:
                ans.append([])
                prevCol = nodeList[i][2]
            ans[-1].append(nodeList[i][0])
        
        return ans
                
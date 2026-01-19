# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        parentMap = {}
        infectedNode = None
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    parentMap[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parentMap[node.right] = node
                    queue.append(node.right)
                if node.val == start:
                    infectedNode = node
        
        time = -1
        visited = set([infectedNode])
        queue = deque([infectedNode])

        while queue:
            size = len(queue)
            time += 1

            for i in range(size):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)

                if node in parentMap and parentMap[node] not in visited:
                    queue.append(parentMap[node])
                    visited.add(parentMap[node])
        return time
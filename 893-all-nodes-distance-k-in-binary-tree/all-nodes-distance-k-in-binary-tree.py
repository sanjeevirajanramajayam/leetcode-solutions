# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parentMap = {}
        queue = deque([root])
        while queue:
            # print(queue)
            node = queue.popleft()
            if node.left:
                parentMap[node.left] = node
                queue.append(node.left)
            if node.right:
                parentMap[node.right] = node
                queue.append(node.right)

        queue = deque([target])
        dist = 0
        visited = set([target])
        while queue:

            if dist == k:
                break
            dist += 1

            size = len(queue)
            for i in range(size):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)

                if node in parentMap and parentMap[node] not in visited:
                    queue.append(parentMap[node])
                    visited.add(parentMap[node])
                    # print(node.val, parentMap[node].val)

                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
        
        return list([node.val for node in queue])
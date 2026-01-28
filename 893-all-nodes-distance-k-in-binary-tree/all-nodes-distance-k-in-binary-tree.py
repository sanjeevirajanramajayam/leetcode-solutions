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
        self.lookingFor = -1
        parentMap = {}
        def preOrder(root):
            if root == None:
                return None
            
            if root.val == target.val:
                self.lookingFor = root
            
            if root.right:
                parentMap[root.right] = root
            
            if root.left:
                parentMap[root.left] = root
            
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)

        # print([[key.val, parentMap[key].val] for key in parentMap])

        queue = deque([self.lookingFor])
        visited = set([self.lookingFor])
        c = 0

        while queue:
            if c == k:
                break
            c += 1 

            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.right and node.right not in visited:
                    queue.append(node.right)

                if node.left and node.left not in visited:
                    queue.append(node.left)

                if node in parentMap and parentMap[node] not in visited:
                    queue.append(parentMap[node])
                
                visited.add(node)
        
        return [x.val for x in queue]
                

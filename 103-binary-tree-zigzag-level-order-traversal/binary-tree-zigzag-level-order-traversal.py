# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque([root])
        res = []

        if not root:
            return res
        flag = True
        while queue:
            size = len(queue)
            temp = [-1] * size 
            # print([x.val for x in queue])
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if flag:
                    temp[i] = (node.val)
                else:
                    temp[size - i - 1] = node.val
            flag = not flag
            # print([x for x in temp])
            res.append(temp)
        
        return res
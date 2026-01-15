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
        ans = []
        flag = True
        if not root:
            return []
        while queue:
            size = len(queue)
            res = [-1] * size
            for i in range(size):
                val = queue.popleft()
                if val:
                    if val.left:
                        queue.append(val.left)
                    if val.right:
                        queue.append(val.right)
                    if flag:
                        res[i] = (val.val)
                    else:
                        res[size - i - 1] = val.val
            if res:
                ans.append(res)
            flag = not flag
        return ans        
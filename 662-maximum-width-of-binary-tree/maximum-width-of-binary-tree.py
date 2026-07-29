# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        ans = 1
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * i + 1))
                if node.right:
                    queue.append((node.right, 2*i + 2))
            mini = float('inf')
            maxi = float('-inf')

            for i in range(len(queue)):
                mini = min(mini, queue[i][1])
                maxi = max(maxi, queue[i][1])

            ans = max(ans, maxi - mini + 1)
        return ans
            
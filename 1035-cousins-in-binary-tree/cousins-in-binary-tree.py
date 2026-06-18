# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        ans = []
        while queue:
            xSeen = False
            ySeen = False
            qLen = len(queue)
            temp = []
            for i in range(qLen):
                picked = False
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    # print(node.left)
                    queue.append(node.left)
                    if not picked:
                        if node.left.val == x:
                            xSeen = True
                            picked = True
                        if node.left.val == y:
                            ySeen = True
                            picked = True
                if node.right:
                    # print(node.right)
                    queue.append(node.right)
                    if not picked:
                        if node.right.val == y:
                            ySeen = True
                            picked = True
                        if node.right.val == x:
                            xSeen = True
                            picked = True
            if xSeen is not False and ySeen is not False:
                return True
            ans.append(temp)
        # print(ans)
        return False

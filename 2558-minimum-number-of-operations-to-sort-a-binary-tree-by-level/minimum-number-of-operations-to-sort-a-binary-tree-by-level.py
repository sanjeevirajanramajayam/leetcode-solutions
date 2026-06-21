# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        		#Code here
        def array(arr):
            indexMap = {}
            sortedArr = sorted(arr)
            
            for i in range(len(arr)):
                indexMap[arr[i]] = i
            swaps = 0
            for i in range(len(arr)):
                if sortedArr[i] != arr[i]:
                    o_i = i
                    o_si = indexMap[sortedArr[i]]
                    
                    indexMap[arr[o_i]] = o_si
                    indexMap[arr[o_si]] = o_i
                    
                    arr[o_i], arr[o_si] = arr[o_si], arr[o_i]
                    
                    swaps += 1
            # print(arr)
            return swaps

        queue = deque([root])
        ans = []
        anss = 0
        while queue:
            qLen = len(queue)
            temp = []
            for i in range(qLen):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            anss += array(temp)
        return anss

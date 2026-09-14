# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freqMap = {}
        def fn(root):
            nonlocal freqMap
            if not root:
                return 0
            
            left = fn(root.left)
            right = fn(root.right)
            freqMap[root.val + left + right] = freqMap.get(root.val + left + right, 0) + 1
            return root.val + left + right
        fn(root)
        maxFreq = float('-inf')
        for key in freqMap:
            maxFreq = max(maxFreq, freqMap[key])
        ans = []
        for key in freqMap:
            if freqMap[key] == maxFreq:
                ans.append(key)
        return ans
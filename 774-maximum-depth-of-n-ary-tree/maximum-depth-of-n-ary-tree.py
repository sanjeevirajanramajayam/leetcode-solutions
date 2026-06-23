"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def traverse(root):
            maxi = float('-inf')
            for child in root.children:
                maxi = max(maxi, traverse(child))
            if maxi == float('-inf'):
                return 1
            return 1 + maxi
        return traverse(root)
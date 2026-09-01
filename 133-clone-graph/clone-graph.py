"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hMap = {}
        def dfs(node):
            if node in hMap:
                return hMap[node]
            
            newNode = Node(node.val)
            hMap[node] = newNode
            for nnode in node.neighbors:
                newNode.neighbors.append(dfs(nnode))
            return newNode
        
        return dfs(node)
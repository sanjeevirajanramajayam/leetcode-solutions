class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, V):
                self.V = V
                self.parent = [i for i in range(V + 1)]
                self.rank = [1 for i in range(V + 1)]
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, u, v):
                u = self.find_parent(u)
                v = self.find_parent(v)

                if self.rank[u] > self.rank[v]:
                    self.parent[v] = u
                elif self.rank[v] > self.rank[u]:
                    self.parent[u] = v
                else:
                    self.rank[v] += 1
                    self.parent[u] = v
                
        maxi = 0
        for startNode, endNode in edges:
            maxi = max(maxi, startNode, endNode) 
        # print(maxi)
        dsu = DSU(maxi)
        cnt = 0
        ans = []
        for startNode, endNode in edges:
            if dsu.find_parent(startNode) != dsu.find_parent(endNode):
                dsu.union(startNode, endNode)
            else:
                ans = [startNode, endNode]
        return ans
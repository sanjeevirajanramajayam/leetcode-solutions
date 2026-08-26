class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class DSU:
            def __init__(self, V):
                self.V = V
                self.parent = [i for i in range(V)]
                self.rank = [0 for i in range(V)]
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node] 
            
            def union(self, u, v):
                uPar = self.find_parent(u)
                vPar = self.find_parent(v)

                if uPar == vPar:
                    return
                
                if self.rank[uPar] > self.rank[vPar]:
                    self.parent[vPar] = uPar 
                elif self.rank[vPar] > self.rank[uPar]:
                    self.parent[uPar] = vPar
                else:
                    self.parent[uPar] = vPar
                    self.rank[vPar] += 1
        dsu = DSU(n)
        extra = 0
        for startNode, endNode in connections:
            if dsu.find_parent(startNode) == dsu.find_parent(endNode):
                extra += 1
            else:
                dsu.union(startNode, endNode)
        nc = 0
        # print(dsu.parent)
        for i in range(n):
            if dsu.parent[i] == i:
                nc += 1
        
        if extra >= nc - 1:
            return nc - 1
        else:
            return -1
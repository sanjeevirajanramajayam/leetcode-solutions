class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        class DSU:
            def __init__(self):
                self.parent = [i for i in range(n)]
                self.rank = [0 for i in range(n)]
            
            def findUPar(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.findUPar(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                Ux = self.findUPar(x)
                Uy = self.findUPar(y)
                if Ux == Uy:
                    return
                
                if self.rank[Ux] > self.rank[Uy]:
                    self.parent[Uy] = Ux
                elif self.rank[Ux] < self.rank[Uy]:
                    self.parent[Ux] = Uy
                else:
                    self.parent[Ux] = Uy
                    self.rank[Uy] += 1
        dsu = DSU()
        for x, y in edges:
            dsu.union(x, y)
        return dsu.findUPar(source) == dsu.findUPar(destination)
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        class DSU:
            def __init__(self):
                self.parent = [i for i in range(n)]
                self.rank = [0] * n
                self.extra = 0

            def uPar(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.uPar(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                uX = self.uPar(x)
                uY = self.uPar(y)

                if uX == uY:
                    self.extra += 1
                    return 

                if self.rank[uX] > self.rank[uY]:
                    self.parent[uY] = uX
                elif self.rank[uX] < self.rank[uY]:
                    self.parent[uX] = uY
                else:
                    self.parent[uX] = uY
                    self.rank[uY] += 1
            
            def get_components(self):
                nc = 0
                for i in range(len(self.parent)):
                    if i == self.parent[i]:
                        nc += 1
                return nc
                
        requiredEdges = n - 1
        dsu = DSU()
        for startNode, endNode in connections:
            dsu.union(startNode, endNode)
        
        nc = dsu.get_components()

        if dsu.extra >= (nc - 1):
            return nc - 1
        else:
            return -1

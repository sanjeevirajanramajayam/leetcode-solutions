class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.n = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
                self.extra = 0
            
            def find_parent(self, node):
                if node == self.parent[node]:
                    return node 
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                rX = self.find_parent(x)
                rY = self.find_parent(y)

                if rX == rY:
                    self.extra += 1
                else:
                    if self.rank[rX] > self.rank[rY]:
                        self.rank[rX] += 1
                        self.parent[rY] = rX
                    elif self.rank[rY] > self.rank[rX]:
                        self.rank[rY] += 1
                        self.parent[rX] = rY
                    else:
                        self.rank[rX] += 1
                        self.parent[rY] = rX

        dsu = DSU(n)

        for start, end in connections:
            dsu.union(start, end)
        
        # print(dsu.extra)
        # print(dsu.parent)
        components = 0
        for i in range(len(dsu.parent)):
            if i == dsu.parent[i]:
                components += 1
        if dsu.extra >= components - 1:
            return components - 1
        else:
            return -1
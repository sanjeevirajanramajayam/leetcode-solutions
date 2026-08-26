class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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
        
        ROWS = 0
        COLS = 0

        for i, j in stones:
            ROWS = max(ROWS, i)
            COLS = max(COLS, j)

        ROWS += 1
        COLS += 1

        dsu = DSU(ROWS + COLS)
        for row, col in stones:
            newCol = col + ROWS
            dsu.union(row, newCol)
        
        # print(dsu.parent)

        roots = set()

        for row, col in stones:
            roots.add(dsu.find_parent(row))
            roots.add(dsu.find_parent(col + ROWS))

        return len(stones) - len(roots)
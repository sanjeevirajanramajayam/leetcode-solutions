class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        class DSU:
            def __init__(self, V):
                self.rank = [0 for i in range(V)]
                self.parent = [i for i in range(V)]
                self.totalWt = 0

            def find_parent(self, node):
                if node == self.parent[node]:
                    return node
                self.parent[node] = self.find_parent(self.parent[node])
                return self.parent[node]
            
            def union(self, x, y):
                xP = self.find_parent(x)
                yP = self.find_parent(y)
                
                if xP == yP:
                    return 
                    
                if self.rank[xP] > self.rank[yP]:
                    self.parent[yP] = xP
                elif self.rank[xP] < self.rank[yP]:
                    self.parent[xP] = yP
                else:
                    self.parent[xP] = yP
                    self.rank[yP] += 1

        colMax = 0
        rowMax = 0
        for i in range(len(stones)):
            colMax = max(colMax, stones[i][1])
            rowMax = max(rowMax, stones[i][0])
        
        dsu = DSU(rowMax + colMax + 2)

        seenStones = set()

        for (row, col) in stones:
            Crow = row
            Ccol = col + rowMax + 1
            dsu.union(Crow, Ccol)
            seenStones.add(Crow)
            seenStones.add(Ccol)
        
        component = 0

        for stone in seenStones:
            if dsu.find_parent(stone) == stone:
                component += 1
        
        return len(stones) - component
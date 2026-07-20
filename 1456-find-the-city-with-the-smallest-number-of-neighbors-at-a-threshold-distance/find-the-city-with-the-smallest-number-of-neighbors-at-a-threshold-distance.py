class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjMat = [[float('inf') for i in range(n)] for i in range(n)]
        for i in range(n):
            adjMat[i][i] = 0
        for s, e, d in edges:
            adjMat[s][e] = (d)
            adjMat[e][s] = (d)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        
        # print(adjMat)
        ans = 0
        maxC = float('inf')
        for i in adjMat:
            cnt = 0
            for j in i:
                if j <= distanceThreshold:
                    cnt += 1
            if cnt <= maxC:
                maxC = cnt
                ans = adjMat.index(i)
        return ans
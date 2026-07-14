class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        adjMat = [[float('inf') for i in range(n)] for i in range(n)]

        for i in range(n):
            adjMat[i][i] = 0

        for startNode, endNode, wt in edges:
            adjMat[startNode][endNode] = wt
            adjMat[endNode][startNode] = wt
        
        # print(adjMat)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        # print(adjMat)
        ans = -1
        mini = float('inf')
        for i in range(n):
            cnt = 0
            for j in range(n):
                if adjMat[i][j] <= dt:
                    cnt += 1
            if cnt <= mini:
                ans = i
                mini = cnt
        return ans
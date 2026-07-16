class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], d: int) -> int:
        adjMat = [[float('inf') for i in range(n)] for i in range(n)]
        for i in range(n):
            adjMat[i][i] = 0
        for startNode, endNode, wt in edges:
            adjMat[startNode][endNode] = wt
            adjMat[endNode][startNode] = wt
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        # print(adjMat)
        maxAns = float('inf')
        ans = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j:
                    if adjMat[i][j] <= d:
                        cnt += 1
            # print(i, cnt)
            if cnt <= maxAns:
                maxAns = cnt
                ans = i
        return ans
            
class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        adjMat = [[float('inf') for i in range(n)] for i in range(n)]
        
        for i in range(n):
            adjMat[i][i] = 0
        
        for s, e in p:
            adjMat[s][e] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][k] + adjMat[k][j])
        
        # print(adjMat)
        ans = []
        for s, e in q:
            if adjMat[s][e] != float('inf'):
                ans.append(True)
            else:
                ans.append(False)
        return ans
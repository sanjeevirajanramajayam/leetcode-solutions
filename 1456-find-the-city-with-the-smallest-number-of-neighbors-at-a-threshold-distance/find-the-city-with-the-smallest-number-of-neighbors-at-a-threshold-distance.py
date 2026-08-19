class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = [[float('inf') for i in range(n)] for i in range(n)]
        for i in range(n):
            mat[i][i] = 0

        for start, end, wt in edges:
            mat[start][end] = wt
            mat[end][start] = wt

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        ans = -1
        mini = float('inf')

        for city in range(n):
            cnt = 0
            for j in range(n):
                if mat[city][j] <= distanceThreshold and mat[city][j] != 0:
                    cnt += 1
            if cnt <= mini:
                mini = cnt
                ans = city
        return ans

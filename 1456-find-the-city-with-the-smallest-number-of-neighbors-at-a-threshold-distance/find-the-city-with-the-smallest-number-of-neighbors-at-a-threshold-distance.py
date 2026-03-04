class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adjMatrix = [[float('inf') for i in range(n)] for i in range(n)]

        for i in range(n):
            adjMatrix[i][i] = 0

        for i in range(len(edges)):
            start, end, wt = edges[i]
            adjMatrix[start][end] = wt
            adjMatrix[end][start] = wt
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])
        
        min_val = float('inf')
        min_node = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if adjMatrix[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_val:
                min_val = count
                min_node = i
        return min_node
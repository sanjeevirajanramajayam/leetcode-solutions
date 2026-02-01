class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        adjList = [[] for _ in range(len(isConnected) + 1)]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    if i != j:
                        adjList[i + 1].append(j + 1)

        count = 0
        visited = [-1 for _ in range(len(isConnected) + 1)]

        def dfs(node):
            visited[node] = 1
            for i in adjList[node]:
                if visited[i] == -1: 
                    dfs(i)
                    # print(i)

        for i in range(1, len(isConnected) + 1):
            if visited[i] == -1:
                dfs(i)
                count += 1
        
        return count
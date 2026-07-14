class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]
        
        for startNode, endNode in p:
            adjList[startNode].append(endNode)
        
        visited = [0] * n
        dfsVisited = [0] * n

        def dfs(i):
            visited[i] = 1
            dfsVisited[i] = 1
            for newNode in adjList[i]:
                if visited[newNode] == 1 and dfsVisited[newNode] == 1:
                    return False
                if visited[newNode] != 1:
                    if not dfs(newNode):
                        return False
            dfsVisited[i] = 0
            return True
        
        for i in range(n):
            if visited[i] == 0: 
                if not dfs(i):
                    return False
        return True

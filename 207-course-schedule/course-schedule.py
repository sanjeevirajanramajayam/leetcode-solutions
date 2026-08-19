class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        dfsVisited = [0] * n
        adjList = [[] for i in range(n)]
        for startNode, endNode in p:
            adjList[endNode].append(startNode)
            # adjList[startNode].append(endNode)
        # print(adjList)
        visited = [0]*n

        def dfs(node):
            visited[node] = 1
            dfsVisited[node] = 1
            for nnode in adjList[node]:
                # print(nnode, node, visited, dfsVisited)
                if visited[nnode] == 1 and dfsVisited[nnode] == 1:
                    return False
                if visited[nnode] != 1:
                    if dfs(nnode) is False:
                        return False
            dfsVisited[node] = 0
        
        for i in range(n):
            if visited[i] == 0:
                if dfs(i) is False:
                    return False
        return True
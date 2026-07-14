class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1 for i in range(len(graph))]
        def dfs(i, color):
            visited[i] = color
            for endNode in graph[i]:
                if visited[endNode] == color:
                    return False
                if visited[endNode] == -1:
                    if not dfs(endNode, not color):
                        return False
            return True
        for i in range(len(graph)):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        return True


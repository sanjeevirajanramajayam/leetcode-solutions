class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1] * len(graph)

        def dfs(i, color):
            visited[i] = color
            for newN in graph[i]:
                if visited[newN] != -1 and visited[newN] == color:
                    return False
                if visited[newN] == -1:
                    if not dfs(newN, not color):
                        return False
            return True
        # print(visited)
        for i in range(len(graph)):
            if visited[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

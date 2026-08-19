class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1] * len(graph)

        def dfs(node, color):
            # print(node, color)
            visited[node] = color
            for nnode in graph[node]:
                if visited[nnode] != -1 and visited[nnode] == color:
                    return False

                if visited[nnode] == -1:
                    ncolor = color

                    if ncolor == 1:
                        ncolor = 0
                    else:
                        ncolor = 1

                    if dfs(nnode, ncolor) is False:
                        return False

        for i in range(len(graph)):
            if visited[i] == -1:
                if dfs(i, 0) is False:
                    return False
        return True

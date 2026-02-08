class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [-1] * len(graph)

        def dfs(node, color):
            visited[node] = color
            for i in graph[node]:
                if visited[i] == -1:
                    if dfs(i, not color):
                        return True
                elif visited[i] == color:
                    return True
            return False
        
        for i in range(len(visited)):
            if visited[i] == -1:
                if dfs(i, 0):
                    return False
        
        return True



class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
            
        visited = [-1 for i in range(len(graph))]
        safeNodes = [-1 for i in range(len(graph))]
        pathAlong = [-1 for i in range(len(graph))]

        def dfs(node):
            visited[node] = 1
            pathAlong[node] = 1

            for i in graph[node]:
                if visited[i] == -1:
                    if dfs(i) == False:
                        safeNodes[node] = 0
                        return False
                if pathAlong[i] == 1:
                    safeNodes[node] = 0
                    return False
            
            pathAlong[node] = 0
            safeNodes[node] = 1
            # print(node)
            return True

        for i in range(len(graph)):
            if visited[i] == -1:
                dfs(i)
        
        res = []
        
        for i in range(len(graph)):
            if safeNodes[i] == 1:
                res.append(i)

        return res
        # print(safeNodes)
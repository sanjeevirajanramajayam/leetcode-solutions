class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        adjList = [[] for i in range(n)]

        for startNode, endNode in connections:
            adjList[startNode].append(endNode)
            adjList[endNode].append(startNode)
        
        low = [0 for i in range(n)]
        time = [0 for i in range(n)]
        visited = [0 for i in range(n)]
        timer = [0]
        bridges = []

        def dfs(node, parent):
            # nonlocal timer
            visited[node] = 1
            time[node] = timer[0]
            low[node] = timer[0] 
            timer[0] += 1

            for newNode in adjList[node]:
                if newNode != parent:
                    if visited[newNode] == 0:
                        dfs(newNode, node)
                        low[node] = min(low[node], low[newNode])
                        if low[newNode] > time[node]:
                            bridges.append([node, newNode])
                            # print(bridges)
                    else:
                        low[node] = min(low[node], low[newNode])

        dfs(0, -1)
        return bridges
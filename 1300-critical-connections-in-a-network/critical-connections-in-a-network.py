class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        timer = 0
        time = [0] * n
        low = [0] * n
        visited = set()
        timer = 0
        adjList = [[] for i in range(n)]
        for startNode, endNode in connections:
            adjList[startNode].append(endNode)
            adjList[endNode].append(startNode)
        ans = []
        def dfs(node, parent):
            nonlocal ans, timer
            print(node, parent)
            time[node] = low[node] = timer
            timer += 1
            visited.add(node)
            for nnode in adjList[node]:
                # print(nnode)
                if nnode == parent:
                    continue
                if nnode not in visited:
                    dfs(nnode, node)
                    low[node] = min(low[nnode], low[node])
                    if low[nnode] > time[node]:
                        ans.append([node, nnode])
                else:
                    low[node] = min(low[nnode], low[node])

        dfs(0, -1)
        return ans
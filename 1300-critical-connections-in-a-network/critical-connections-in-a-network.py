class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        tin = [0] * n # when i touched you
        time = 0
        low = [0] * n # lowest apart from parent
        adjList = [[] for i in range(n)]
        for start, end in connections:
            adjList[start].append(end)
            adjList[end].append(start)
        
        visited = set([0])
        ans = []

        def dfs(node, parent):
            nonlocal ans, time
            tin[node] = low[node] = time
            time += 1
            visited.add(node)

            for nnode in adjList[node]:
                if nnode == parent:
                    continue
                
                if nnode not in visited:
                    dfs(nnode, node)
                    low[node] = min(low[node], low[nnode])
                    if low[nnode] > tin[node]:
                        ans.append([node, nnode])   
                else:
                    low[node] = min(low[node], tin[nnode])
        dfs(0, -1)
        return ans
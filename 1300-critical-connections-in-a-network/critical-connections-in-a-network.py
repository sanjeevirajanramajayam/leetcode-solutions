class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        low = [0] * n
        tin = [0] * n
        time = 0
        visited = set([0])
        ans = []
        adjList = [[] for i in range(n)]

        for start, end in connections:
            adjList[start].append(end)
            adjList[end].append(start)

        def dfs(node, parent):
            nonlocal time
            low[node] = tin[node] = time
            time += 1
            visited.add(node)
            # print(node, parent, low, tin, time)

            for nnode in adjList[node]:
                if nnode == parent:
                    continue
                if nnode not in visited:
                    dfs(nnode, node)
                    # print(nnode, node)
                    # print(low, tin)
                    low[node] = min(low[node], low[nnode])
                    if low[nnode] > tin[node]:
                        ans.append([node, nnode])
                else:
                    low[node] = min(low[node], tin[nnode])
        dfs(0, -1)
        return ans
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        timer = 0
        time = [0 for i in range(n)]
        low = [0 for i in range(n)]

        adjList = [[] for i in range(n)]

        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
        ans = []
        visited = set()
        def dfs(node, parent):
            nonlocal ans, timer
            time[node] = low[node] = timer
            timer += 1
            visited.add(node)
            for nnode in adjList[node]:
                if nnode == parent:
                    continue
                if nnode not in visited:
                    dfs(nnode, node)
                    if low[nnode] > time[node]:
                        ans.append([node, nnode])
                    low[node] = min(low[node], low[nnode])
                else:
                    low[node] = min(low[node], low[nnode])
        dfs(0, -1)
        return ans

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        dist = [float('inf') for i in range(n)]
        dist[n - 1] = 0
        adjList = [[] for i in range(n)]
        for startNode, endNode, wt in edges:
            adjList[startNode - 1].append((endNode - 1, wt))
            adjList[endNode - 1].append((startNode - 1, wt))
        
        # print(adjList)

        pq = [(0, n - 1)]
        while pq:
            dt, node = heapq.heappop(pq)
            for nnode, wt in adjList[node]:
                # print(node, nnode)
                if dist[node] + wt < dist[nnode]:
                    dist[nnode] = dist[node] + wt
                    heapq.heappush(pq, (dist[nnode], nnode))
        # print(dist)
        @cache
        def fn(ind):
            if ind == 0:
                return 1
            ans = 0
            for nnode, wt in adjList[ind]:
                if dist[nnode] > dist[ind]:
                    # print(dist[nnode], dist[ind], nnode, ind)
                    ans += fn(nnode)
            return ans
        return fn(n - 1) % (10 ** 9 + 7)
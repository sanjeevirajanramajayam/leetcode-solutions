class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ways = [0] * n
        ways[0] = 1
        # queue = deque([])
        pq = [(0, 0)]
        adjList = [[] for i in range(n)]
        for s, e, dt in roads:
            adjList[s].append((e, dt))
            adjList[e].append((s, dt))
        dist = [float('inf')] * n
        dist[0] = 0
        while pq:
            time, u = heapq.heappop(pq)
            if time > dist[u]:
                continue
            for nnode, dt in adjList[u]:
                if dist[u] + dt < dist[nnode]:
                    dist[nnode] = dist[u] + dt
                    heapq.heappush(pq, (dist[nnode], nnode))
                    ways[nnode] = ways[u]
                elif dist[u] + dt == dist[nnode]:
                    ways[nnode] += ways[u]
        # print(ways, dist)
        return ways[n - 1] % (10 ** 9 + 7)

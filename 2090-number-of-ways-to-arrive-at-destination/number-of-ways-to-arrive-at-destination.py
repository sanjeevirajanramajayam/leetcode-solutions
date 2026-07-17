class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ways = [0] * n
        ways[0] = 1
        pq = [(0, 0)]
        adjList = [[] for i in range(n)]
        dist = [float('inf') for i in range(n)]
        dist[0] = 0
        for s, e, t in roads:
            adjList[s].append((e, t))
            adjList[e].append((s, t))

        while pq:
            dt, node = heapq.heappop(pq)
            if dt > dist[node]:
                continue
            for nnode, wt in adjList[node]:
                if dist[node] + wt < dist[nnode]:
                    dist[nnode] = dist[node] + wt
                    ways[nnode] = ways[node]
                    heapq.heappush(pq, (dist[nnode], nnode))
                elif dist[node] + wt == dist[nnode]:
                    ways[nnode] += ways[node]
        # print(ways)
        return ways[-1] % ((10 ** 9) + 7)

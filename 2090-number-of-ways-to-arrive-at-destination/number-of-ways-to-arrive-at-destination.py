class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        ways = [1 for i in range(n)]
        adjList = [[] for i in range(n)]
        for startNode, endNode, dist in roads:
            adjList[startNode].append((endNode, dist))
            adjList[endNode].append((startNode, dist))
        dist = [float('inf') for i in range(n)]
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nnode, dt in adjList[node]:
                if dist[node] + dt < dist[nnode]:
                    dist[nnode] = dist[node] + dt
                    heapq.heappush(pq, (dist[nnode], nnode))
                    ways[nnode] = ways[node]
                elif dist[node] + dt == dist[nnode]:
                    ways[nnode] += ways[node]
        # print(dist)  
        # print(ways)
        return ways[-1] % (10**9 + 7)
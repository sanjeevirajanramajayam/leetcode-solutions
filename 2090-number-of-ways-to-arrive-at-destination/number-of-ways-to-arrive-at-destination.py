class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        pq = [(0, 0)]
        ways = [0] * n
        ways[0] = 1
        dist = [float('inf')] * n
        dist[0] = 0
        adjList = [[] for i in range(n)]
        for start, end, w in roads:
            adjList[start].append((end, w))
            adjList[end].append((start, w))
        
        while pq:
            dt, node = heapq.heappop(pq)
            # print(dt, node)
            for newNode, wt in adjList[node]:
                if dt + wt < dist[newNode]:
                    dist[newNode] = dt + wt
                    ways[newNode] = ways[node]
                    heapq.heappush(pq, (dist[newNode], newNode))
                elif dt + wt == dist[newNode]:
                    ways[newNode] += ways[node]
        # print(ways)
        return ways[-1] % (10 ** 9 + 7)

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf') for i in range(n)]
        dist[src] = 0
        for _ in range(k+1):
            newDist = dist.copy()
            for start, end, cost in flights:
                if dist[start] != float('inf'):
                    newDist[end] = min(newDist[end], dist[start] + cost)
            # print(newDist)
            dist = newDist
        if newDist[dst] == float('inf'):
            return -1
        return newDist[dst]
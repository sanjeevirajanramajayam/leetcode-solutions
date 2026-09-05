from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adjList = [[] for _ in range(n + 1)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        first = [float('inf')] * (n + 1)
        second = [float('inf')] * (n + 1)

        heap = [(0, 1)]

        while heap:
            dist, node = heappop(heap)

            if dist < first[node]:
                first[node] = dist

            elif first[node] < dist < second[node]:
                second[node] = dist

            else:
                continue

            if node == n and second[node] != float('inf'):
                return second[node]

            # Traffic light
            if (dist // change) % 2 == 1:
                dist += change - (dist % change)

            newDist = dist + time

            for neighbor in adjList[node]:
                heappush(heap, (newDist, neighbor))
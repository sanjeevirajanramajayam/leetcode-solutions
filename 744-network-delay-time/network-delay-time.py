class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adjList = [[] for i in range(n + 1)]

        for startNode, endNode, dist in times:
            adjList[startNode].append((endNode, dist))
        
        pq = [(0, k)]
        distArray = [float('inf') for i in range(n + 1)]
        distArray[k] = 0

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distArray[node]:
                continue
            for newNode, distance in adjList[node]:
                if distArray[node] + distance < distArray[newNode]:
                    distArray[newNode] = distArray[node] + distance
                    heapq.heappush(pq, (distArray[newNode], newNode))
        maxTime = float('-inf')
        for i in range(1, len(distArray)):
            if distArray[i] == float('inf'):
                return -1
            maxTime = max(maxTime, distArray[i])
        
        return maxTime
                
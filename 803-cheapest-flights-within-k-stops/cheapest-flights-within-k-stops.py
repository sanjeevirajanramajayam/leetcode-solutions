class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adjList = [[] for i in range(n)]

        for startNode, endNode, cost in flights:
            adjList[startNode].append((endNode, cost))

        pq = deque([(0, src, 0)])
        distArray = [float('inf') for i in range(n)]
        distArray[src] = 0

        while pq:
            stops, node, dist = pq.popleft()
            if node == dst:
                continue
            for newNode, edW in adjList[node]:
                if edW + dist < distArray[newNode] and stops <= k:
                    distArray[newNode] = edW + dist
                    pq.append((stops + 1, newNode, distArray[newNode]))
        if distArray[dst] == float('inf'):
            return -1
        return distArray[dst]